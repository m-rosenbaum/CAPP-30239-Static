import json
import pathlib
import polars as pl
import sqlite3
import sys


#######################################
# 0. Hard coded references
#######################################
PATHS = (
    "G:/My Drive/CAPP/2025_Q1_CAPP 30239/Data/ar203.csv",
    "G:/My Drive/CAPP/2025_Q1_CAPP 30239/Data/ar539.csv",
)
SCHEMA = "C:/Users/micha/Documents/CAPP/CAPP-30239/CAPP-30239-Static/Data/db.sql"
DB = "C:/Users/micha/Documents/CAPP/CAPP-30239/CAPP-30239-Static/Data/ui_stats.db"


#######################################
# 1. Cleaning functions
#######################################
def clean_eta_203(file: str, names: dict) -> pl.DataFrame:
    """
    Takes in a location (either URL or CSV) for the ETA 539 report and then
    creates a dataframe at the state- month-level that will be iteratively
    passed into the database.

     Input:
        -file (str): Path to location of the ETA 203 file
        -names (dict): Column names to rename

    Output: df (pl.DataFrame): transformed 203 to post to database
    """
    # Run import and rename
    df = pl.read_csv(file)
    df = df.rename(names)
    df = df.select("st", "dt", pl.col(r"^(gen|eth|rac|age)_.*$"))

    # Create month and date
    df = df.with_columns(pl.col("dt").str.to_date(format="%-m/%-d/%Y", strict=True))
    df = df.with_columns(
        pl.col("dt").dt.month().alias("dt_m"), pl.col("dt").dt.year().alias("dt_y")
    )
    df = df.drop("dt")

    # Return file
    return df


def clean_eta_539(file: str, names: dict) -> pl.DataFrame:
    """
    Takes in a location (either URL or CSV) for the ETA 539 report and then
    creates a dataframe at the state- month-level that will be iteratively
    passed into the database.

    Since ETA 539 is at the benefit week (end)-level, this converts data to the
    month-level.

    Input:
        -file (str): Path to location of the ETA 539 file

    Output: df (pl.DataFrame): transformed 539 to post to database
    """
    # Run import and rename
    df = pl.read_csv(file)
    df = df.rename(names)
    df = df.select(
        "st",
        "dt",
        "wk_num",
        "ct_ic",
        "ct_fic",
        "ct_xic",
        "ct_wks",
        "ct_wks_f",
        "ct_wks_x",
        "ct_wks_eb",
        "rt_recip",
        "ind_eb",
        "dt_eb",
    )

    # Handle unit of observations shift
    # TODO: Check how this is handled by the ETA. Not in documentation here.
    df = df.with_columns(pl.col("dt").str.to_date(format="%-m/%-d/%Y", strict=True))
    df = df.with_columns(
        pl.col("dt").dt.month().alias("dt_m"), pl.col("dt").dt.year().alias("dt_y")
    )

    # Collapse to month-level
    # Ref: https://stackoverflow.com/a/74902919
    df = df.group_by(["st", "dt_m", "dt_y"]).agg(
        pl.col(r"^(ct)_.*$").sum(),
        # Unweighted avg as data is meaned on time, not population
        pl.col(r"^(rt)_.*$").mean(),
    )

    return df


def load_encoding(file: str) -> dict:
    """
    Takes in a file stored as json and converts it to a dictionary. Used to run
    renaming across wider ETA datasets pulled in.

    Input:
        file (str): path to file names

    Output: dict()
    """
    names = json.load(open(file))
    return names


#######################################
# 2. Functions to create and write to DB
#######################################
def make_db(db: str, schema: str) -> None:
    """
    Create sqlite3 database from saved schema

    Input:
        db (str): Path to database file
        schema (str): Path to script that contains schema

    Output: None (creates database at path)
    """
    # First generate path
    path_db = pathlib.Path(db)
    if path_db.is_file():
        path_db.unlink()  # Delete if it exists already

    # Create a new connection to a path
    conn = sqlite3.connect(path_db)
    c = conn.cursor()

    # Create table for both schems
    with open(schema, "r") as script:
        c.executescript(script.read())
    conn.commit()
    c.close()


def load_data(db: str, df: pl.DataFrame, table: str) -> None:
    """
    Write a Polars dataframe into a database with inserting only new columns.

    Input:
        db (str): Path to database
        df (pl.DataFrame): Polars dataframe to write to
        table (str): Name of the table to write to.

    Output: None, writes to database in input
    """
    # Create a new connection to a databse
    path = pathlib.Path(f"{db}")
    conn = sqlite3.connect(path)
    c = conn.cursor()

    # Build parameter lists
    keys = []
    params = []
    for key in df.columns:
        keys.append(f"{key}")
        params.append(f":{key}")  # sqlit3 package uses :name to specify a col

    # Create query to write line by line
    query = f"INSERT OR IGNORE INTO {table} ({', '.join(keys)}) VALUES ({', '.join(params)})"
    print(f"{query}")

    # Write file
    c.executemany(query, df.rows(named=True))
    conn.commit()

    # Commit and close
    conn.close()


#######################################
# 3. Run cleaning script
#######################################
if __name__ == "__main__":

    # Check that two arguments exist
    if len(sys.argv) != 3 and len(sys.argv) != 1:
        raise SyntaxError(
            f"Missing arguments. You must either no arguments or two files:"
            f"  - Location of the ETA 203 csv to pass to pl.read_csv()"
            f"  - Location of the ETA 539 csv to pass to pl.read_csv()"
            f"If no files supplied, it will use locations on Michael's Drive"
        )

    # Grab file paths
    if len(sys.argv) == 1:
        path_203 = PATHS[0]
        path_539 = PATHS[1]
    else:
        path_203 = sys.argv[1]
        path_539 = sys.argv[2]

    # Import and clean files
    names_203 = load_encoding(pathlib.Path().resolve() / "eta_203_names.json")
    names_539 = load_encoding(pathlib.Path().resolve() / "eta_539_names.json")
    df_203 = clean_eta_203(path_203, names_203)
    df_539 = clean_eta_539(path_539, names_539)

    # Write to db
    path_db = pathlib.Path(DB)
    if not path_db.is_file():
        print("Made it")
        make_db(DB, SCHEMA)
    load_data(DB, df_203, "ui_demos")
    load_data(DB, df_539, "ui_cts")
