import altair as alt
import polars as pl
from datetime import datetime


def c1(file) -> alt.Chart:
    """
    Writes a graph describing federal unemployment recipiency.

    Input:
        file (pl.DataFrame): File with federal unemployment

    Returns (Chart): Chart object
    """
    c1 = (
        alt.Chart(
            file.to_pandas(),
            title=alt.Title(
                "Since 2007, about 30 percent of unemployed Americans receive unemployment insurance",
                subtitle="Unemployment insurance recipiency, annual moving average: 2007-2019",
            ),
        )
        .mark_line(strokeWidth=3)
        .encode(
            alt.X("date:T").title(None),
            # Ref: https://stackoverflow.com/a/62282675
            alt.Y("rt_recip", scale=alt.Scale(domain=[0, 1]))
            .axis(format="%")
            .title("Recipiency rate"),
        )
    ).properties(width=600)

    # text = alt.Chart(file).mark_text(
    #    text='"Data: The Century Foundation (2024). Unemployment Data Dashboard"',
    #    x=0,
    #    y="height",
    #    dx=0,
    #    dy=30,
    #    fontWeight="normal",
    #    fontSize=8,
    # )

    return c1
