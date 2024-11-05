# Imports
import altair as alt
import os
import sqlite3
import polars as pl
import textwrap

alt.data_transformers.enable("vegafusion")

# Import graph code
from charts.theme_unemp import unemp_theme
from data_processing import load_fed, load_st, load_example_ui_data, subset_sts
from charts.c1 import c1
from charts.c2 import c2
from charts.c3 import c3
from charts.c4 import c4
from charts.c5 import c5
from charts.c6 import c6
from charts.c7 import c7
from charts.c8 import c8

# Run data processing and chart generation
if __name__ == "__main__":

    # Manage altair
    alt.themes.register("unemp_theme", unemp_theme)
    alt.themes.enable("unemp_theme")

    # Get data
    fed = load_fed()
    st = load_st()
    elig_df, ic_df, claimed_df = load_example_ui_data()
    filt_2019 = (pl.col("dt_m") == 12, pl.col("dt_y") == 2019)

    # Load states
    # Ref for handling GEOJSON: https://stackoverflow.com/questions/67283970/altair-choropleth-adding-values-associated-with-each-county-to-the-map
    # Ref: "https://raw.githubusercontent.com/vega/vega-datasets/master/data/us-10m.json"
    url = "https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json"
    geo = alt.topo_feature(url, "states")

    # Run each chart sequentially
    c1 = c1(fed.filter(pl.col("date") < pl.date(year=2020, month=1, day=1)))
    c2 = c2(elig_df, ic_df, claimed_df)
    c3 = c3(
        fed.filter(pl.col("date") < pl.date(year=2020, month=1, day=1)),
        st.filter(pl.col("date") < pl.date(year=2020, month=1, day=1)),
    )
    c4 = c4(st)
    c5 = c5(st)
    # c6 = c6(st) # Dropping this chart
    c7 = c7(st, geo, fed, filt_2019)
    c8 = c8(subset_sts(st))

    # Run and save
    save_list = [c1, c2, c3, c4, c5, c7, c8]
    skip_list = [5]  # Issues with date coersion out of Jupyter
    i = 0
    for chart in save_list:
        # Advance chart name counter
        i += 1
        print("Working on: ", i)
        if i in skip_list:
            continue

        # Get parent directory
        root = os.path.join(os.path.abspath(""), os.path.pardir)
        loc = os.path.join(root, "static_final", f"c{i}.svg")

        # Save to parent dir
        chart.save(f"{loc}")
