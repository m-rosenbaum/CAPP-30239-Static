import altair as alt


def c5(st) -> alt.Chart:
    """
    Writes a graph describing federal unemployment recipiency with underlayed
    state recipiency rates.

    Input:
        file (pl.DataFrame): File with federal unemployment

    Returns (Chart): Chart object
    """
    c5_st = (
        alt.Chart(
            st,
            title=alt.Title(
                "This picture gets complicated. States had over 100 percent recipiency during the COVID-19 pandemic due to loosened eligibility requirements",
                subtitle="Recipiency rate by state: 2006-2024, annually smoothed",
            ),
        )
        .mark_line(color="#33333340", strokeWidth=1)
        .encode(
            alt.X("date:T").title(None),
            alt.Y("rt_recip", scale=alt.Scale(domain=[0, 1.5]))
            .title("Recipinecy Rate")
            .axis(format="%"),
            # Detail approach from https://github.com/vega/altair/issues/985
            detail="st",
        )
    )

    # Ref for highlighting: https://altair-viz.github.io/gallery/bar_chart_with_single_threshold.html
    threshold = 1
    st_highlight = (
        alt.Chart(st)
        .mark_line(color="#BF4E00")
        .encode(alt.X("date:T").title(None), alt.Y("rt_recip"), detail="st")
        .transform_filter(alt.datum.rt_recip > threshold)
    )

    # Add in line
    rule = (
        alt.Chart()
        .mark_rule(color="#203440", strokeWidth=2)
        .encode(y=alt.Y(datum=threshold))
    )
    label = rule.mark_text(
        x="width",
        dx=-2,
        align="right",
        baseline="bottom",
        text="More than 100% recipiency",
        color="#BF4E00",
    )

    c5 = c5_st + st_highlight + rule + label
    return c5
