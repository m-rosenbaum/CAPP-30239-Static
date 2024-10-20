import os
import sqlite3
import polars as pl

# Hardcoded values
DB_PATH = os.path.join(os.path.abspath(""), os.path.pardir, "data", "ui_stats.db")
QUERY_ST = """
    SELECT 
        ui_cts.st as st, ui_cts.dt_m as dt_m, ui_cts.dt_y as dt_y, ct_wks_12mo, 
        ct_u3_12mo, unemp.rt_recip as rt_recip
    FROM 
        ui_cts 
    JOIN 
        unemp ON ui_cts.st = unemp.st AND 
        ui_cts.dt_m = unemp.dt_m AND 
        ui_cts.dt_y = unemp.dt_y
    WHERE 
        ui_cts.dt_y > 2006
    ;
"""
QUERY_DEMOS = """
    SELECT 
        * 
    FROM 
        ui_demos 
    WHERE 
        dt_y > 2006
    ;
"""


#######################################
# Data Call functions
#######################################
def query():
    """
    Queries the DB to extract the recipiency data

    Inputs: None

    Returns: pl.DataFrame of state_level data frame
    """
    # Establish
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Execute two queries and extract column names
    # Ref to extract column names: https://stackoverflow.com/a/7831685
    c.execute(QUERY_ST)
    result = c.fetchall()

    cols = []
    for elem in c.description:
        cols.append(elem[0])

    # No demos for now
    # c.execute(demos_st)
    # st_demos = c.fetchall()
    # cols_demos = []
    # for elem in c.description:
    #    cols_demos.append(elem[0])

    conn.close()

    # Now convert to Polars object for plotting
    results_df = pl.DataFrame(result, schema=cols, orient="row").with_columns(
        pl.date(year=pl.col("dt_y"), month=pl.col("dt_m"), day=1).alias("date")
    )

    return results_df


def load_st():
    """
    Wrapper for query to load state counts database. Written to use query() as
    a helper function if there's multiple tables to query.

    Returns (pl.DataFrame): state_level data frame
    """
    st_cts_df = query()
    return st_cts_df


def load_fed():
    """
    Load and aggregate state-level data-frame

    Returns (pl.DataFrame): federal-level data frame
    """
    st_cts_df = load_st()

    # Aggregate to the month-level
    fed_cts_df = (
        st_cts_df.group_by("dt_m", "dt_y")
        .agg(pl.exclude("dt_m", "dt_y", "date", "rt_recip").sum(), pl.col("date").max())
        .with_columns((pl.col("ct_wks_12mo") / pl.col("ct_u3_12mo")).alias("rt_recip"))
    )

    return fed_cts_df


def load_example_ui_data():
    """
    Create example data for to illustrate 4 cases of UI behavior: (1) Does not
    apply, (2) Exhaust at 26 weeks, (3) Exhaust at 12 weeks, and (4) some
    weekly certifications not filed. Creates three dataframes to pass to
    Altair code to illustrate this behavior.

    Input (None)

    Returns: (DataFrame, DataFrame, DataFrame)
    """
    # Create lists
    elig_y = []
    elig_x = []
    ic_y = []
    ic_x = []
    claimed_y = []
    claimed_x = []

    # Fill lists with relevant data
    for y in range(1, 5):
        for x in range(1, 27):

            # Skip Florida > 12 weeks
            if y == 3 and x > 12:
                continue

            # Always eligible if not in Florida
            elig_y.append(y)  # Always has a y value
            elig_x.append(x)

            # Skip no initial claim filer
            if y == 1:
                continue

            ic_y.append(y)
            ic_x.append(x)

            # Remove missed weeks
            if y == 2:
                if x in (1, 4, 5, 13, 16):
                    continue

            # Append claimed
            claimed_y.append(y)
            claimed_x.append(x)

    # Load as data frames
    elig_df = pl.DataFrame({"y": elig_y, "elig": elig_x})
    ic_df = pl.DataFrame({"y": ic_y, "ic": ic_x})
    claimed_df = pl.DataFrame({"y": claimed_y, "claimed": claimed_x})

    return elig_df, ic_df, claimed_df
