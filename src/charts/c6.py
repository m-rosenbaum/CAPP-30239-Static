import altair as alt


# 6 - Show recipiency by state in high density heatmap
# Exact reference: https://altair-viz.github.io/gallery/lasagna_plot.html
def c6(st) -> alt.Chart:
    """
    Writes a lasagna graph to show radical break on key states for recipiency
    with the pandemic.

    Input:
        file (pl.DataFrame): File with federal unemployment

    Returns (Chart): Chart object
    """
    c6 = (
        alt.Chart(
            st,
            title=alt.Title(
                "Let's look back at the states with the highest unemployment volume",
                subtitle="Recipiency rate by state: 2006-2023, annually smoothed",
            ),
        )
        .mark_rect()
        .encode(
            alt.X("date")
            .axis(
                format="%Y",
                labelAngle=0,
                labelOverlap=False,
            )
            .title(None),
            alt.Y("st:N").title(None).axis(grid=False).sort("ascending"),
            # Syntax reference for scale: https://stackoverflow.com/q/70295909
            alt.Color(
                "rt_recip:Q",
                scale=alt.Scale(
                    domain=[0, 0.5, 1.5], range=["white", "#0076BF", "#BF4E00"]
                ),
            ).title("Recipiency rate"),
        )
        .transform_filter(
            (alt.datum.st == "PA")
            | (alt.datum.st == "IL")
            | (alt.datum.st == "NJ")
            | (alt.datum.st == "TX")
            | (alt.datum.st == "CA")
            | (alt.datum.st == "NY")
        )  # TODO: Fix to preprocess
    )

    return c6
