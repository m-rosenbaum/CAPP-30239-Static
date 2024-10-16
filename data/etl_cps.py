import json
import pathlib
import polars as pl
import sqlite3

#######################################
# 0. Hard coded references
#######################################
DB = pathlib.Path(__file__).parent / "ui_stats.db"
KEEPVARS = [
    "hrhhid",
    "hrmonth",
    "hryear4",
    "gestfips",  # IDs
    "pemlr",
    "pedwwnto",
    "pehrftpt",  # UI Vars
    "gtco",
    "gtcbsa",  # Urbanicity
    "prtage",
    "pemaritl",
    "pesex",
    "peeduca",
    "ptdtrace",
    "prdthsp",
    "pehspnon",
    "prcitshp",
    "pudis",  # Demographics
    "hwhhwgt",
    "pwsswgt",
    "pwcmpwgt",
    "hrintsta",  # Weights
]
STATES_PATH = pathlib.Path(__file__).parent / "st_fips.json"
STATES = json.load(open(STATES_PATH))


#######################################
# 1. Cleaning functions
#######################################
def clean_cps(file: str) -> pl.DataFrame:
    """
    Takes in a location (either URL or CSV) for an NBER Current Population
    Survey extract and creates a dataframe at the state- month-level that
    will be iteratively passed into the database.

     Input:
        -file (str): Path to location of the ETA 203 file

    Output: df (pl.DataFrame): transfored CPS DataFrame
    """
    # Load file, and read 10,000 lines in to capture int / float
    df = pl.read_csv(file, infer_schema_length=10000).select(KEEPVARS)

    # Remove non-interviews
    df = df.filter(~df["hrintsta"].is_in([2, 3, 4]))

    # Convert all weights to frequency weights from integer formatted wieghts
    wtcols = ["hwhhwgt", "pwsswgt", "pwcmpwgt"]
    for wtcol in wtcols:
        if df["hwhhwgt"].mean() > 10e5:
            df.with_columns(pl.col(wtcol) / 10000)
            assert df[wtcol].mean() <= 10e5  # No freq weights above 10000

    # Create unemployed variables
    # Ref: https://stackoverflow.com/questions/74967585/check-if-python-polars-dataframe-row-value-exists-within-a-defined-list
    df = df.with_columns(
        pl.col("pemlr").is_in([3, 4]).cast(pl.Int8).alias("unemployed"),
        pl.col("pemlr").is_in([1, 2, 3, 4]).cast(pl.Int8).alias("labor_force"),
        (pl.col("pedwwnto") == 1).cast(pl.Int8).alias("marginally_attached"),
        (pl.col("pehrftpt") == 1).cast(pl.Int8).alias("pt_forecon"),
    )

    # Create unemployment rate dummies
    df = df.with_columns(
        pl.when(pl.col("unemployed") == 1)
        .then(1)
        .when(pl.col("marginally_attached") == 1)
        .then(None)
        .otherwise(0)
        .alias("u3"),
        pl.when(pl.col("unemployed") == 1)
        .then(1)
        .when(pl.col("marginally_attached") == 1)
        .then(1)
        .when(pl.col("pt_forecon") == 1)
        .then(1)
        .otherwise(0)
        .alias("u6"),
        pl.when(pl.col("labor_force") == 1).then(1).otherwise(0).alias("lf_u3"),
        pl.when(pl.col("labor_force") == 1)
        .then(1)
        .when(pl.col("marginally_attached") == 1)
        .then(1)
        .otherwise(0)
        .alias("lf_u6"),
    )

    # Then multiply by weight to get actual frequencies
    # Use pwsswgt (final CPS weight), not pwcmpwgt (BLS weight)
    wt = "pwsswgt"
    for col_nm in ["u3", "u6", "lf_u3", "lf_u6"]:
        df = df.with_columns((pl.col(col_nm) * pl.col(wt)).alias(f"ct_{col_nm}"))

    # Then collapse down to the state month-level
    df = df.group_by(["gestfips", "hrmonth", "hryear4"]).agg(
        pl.col(r"^(ct)_.*$").sum(),
    )

    # Ref: Chat-GPT to figure out the polars casting names
    # Recast values and rename
    df = df.with_columns(pl.col("gestfips").cast(pl.Utf8).replace(STATES))
    df.rename({"gestfips": "st", "hrmonth": "dt_m", "hryear4": "dt_y"})

    return df
