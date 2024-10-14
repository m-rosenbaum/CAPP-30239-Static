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
DB = ""


#######################################
# 1. Cleaning functions
#######################################
def clean_eta_203(file) -> pl.DataFrame:
    """ """
    pass


def clean_eta_539(file) -> pl.DataFrame:
    """ """
    pass


#######################################
# 2. Functions to create and write to DB
#######################################
def write_db(str) -> None:
    """ """
    pass


def load_data(file, str) -> None:
    """ """
    pass


#######################################
# 3. Run cleaning script
#######################################
if __name__ == "__main__":

    # Check that two arguments exist
    if len(sys.argv) != 3 or len(sys.argv) != 1:
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
    df_203 = clean_eta_203(path_203)
    df_539 = clean_eta_539(path_539)

    # Write to db
    if not DB:  # TODO - add check if the file exist
        write_db(DB)
    load_data(df_203, "ui_demos")  # TODO - write
    load_data(df_539, "ui_cts")
