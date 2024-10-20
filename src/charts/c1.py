import altair as alt


def c1(file) -> alt.Chart:
    """
    Writes a graph describing federal unemployment recipiency.

    Input:
        file (pl.DataFrame): File with federal unemployment

    Returns (Chart): Chart object
    """
    return (
        alt.Chart(
            file,
            title=alt.Title(
                "Recipiency is how the Department of Labor measures what percentage of unemployed workers receive unemployment insurance.",
                subtitle="Unemployment insurance recipiency, annual moving average: 2006-2019",
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
    )
