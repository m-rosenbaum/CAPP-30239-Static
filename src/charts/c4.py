import altair as alt


def c4(st) -> alt.Chart:
    """
    Writes a graph describing unemployment recipiency as counts, not as rates.

    Input:
        file (pl.DataFrame): File with federal unemployment

    Returns (Chart): Chart object
    """
    # Create bar for unemployment rate
    c4_u3 = (
        alt.Chart(
            st,
            title=alt.Title(
                "Some states also have a larger labor market and then have an outsize influence on recipiency",
                subtitle="Average claims per week 2019",
            ),
        )
        .mark_bar(color="#33333360")
        .encode(
            alt.X("st:N").title("State").sort(field="ct_u3_12mo", order="descending"),
            alt.Y("ct_u3_12mo:Q").title("Count"),
        )
    )

    # Create bar for fill
    c4_ui = (
        alt.Chart(st)
        .mark_bar()
        .encode(
            alt.X("st:N").title("State").sort(field="ct_u3_12mo", order="descending"),
            alt.Y("ct_wks_12mo:Q").title("Count"),
        )
    )

    # Filter to a single year
    c4 = (c4_u3 + c4_ui).transform_filter(
        (alt.datum.dt_y == 2019) & (alt.datum.dt_m == 12)
    )

    # Return stacked object
    return c4
