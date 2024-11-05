import altair as alt


def c3(fed, st) -> alt.Chart:
    """
    Writes a graph describing federal unemployment recipiency with underlayed
    state recipiency rates.

    Input:
        file (pl.DataFrame): File with federal unemployment

    Returns (Chart): Chart object
    """
    # Create federal overlay
    c3_fed = (
        alt.Chart(fed)
        .mark_line(strokeWidth=3)
        .encode(
            alt.X("date:T").title(None),
            alt.Y("rt_recip", scale=alt.Scale(domain=[0, 1]))
            .axis(format="%")
            .title("Recipiency rate"),
        )
        .transform_filter(
            alt.FieldLTPredicate(
                field="date", lt=alt.DateTime(year=2020, month=1, day=1)
            )
        )
    ).properties(width=600)

    # Create state underlay layer
    c3_st = (
        alt.Chart(
            st,
            title=alt.Title(
                "The federal average hides a lot of variation between states",
                subtitle="Unemployment insurance recipiency by state, annual moving average: 2006-2019",
            ),
        )
        .mark_line(color="#33333330", strokeWidth=0.75)
        .encode(
            alt.X("date:T").title(None),
            alt.Y("rt_recip", scale=alt.Scale(domain=[0, 1])),
            # Detail approach from https://github.com/vega/altair/issues/985
            detail="st",
        )
        .transform_filter(
            alt.FieldLTPredicate(
                field="date", lt=alt.DateTime(year=2020, month=1, day=1)
            )
        )
    ).properties(width=600)

    # Stack graphs appropriately
    c3 = c3_st + c3_fed
    return c3
