import altair as alt


def c7(st, geo, fed, filt) -> alt.Chart:
    """
    Writes a chloropleth map to show geographic variation in recipiency.

    Input:
        st(pl.Dataframe): State recipiency rates
        geo (GeoJSON): Altair modified GeoJSON file
        fed(pl.Dataframe): Federal recip
        filt (cond): Filter conditions

    Returns (Chart): Chart object
    """
    # Ref from: https://altair-viz.github.io/gallery/choropleth.html
    c7 = (
        alt.Chart(
            geo,
            title=alt.Title(
                "Recipiency varies geographically.",
                subtitle="Average recipiency in 2019, annually smoothed. Orange is below average, blue is above average",
            ),
        )
        .mark_geoshape()
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(st.filter(filt), "id", ["rt_recip"]),
        )
        .encode(
            alt.Color(
                "rt_recip:Q",
                scale=alt.Scale(
                    domain=[0, fed.filter(filt)["rt_recip"].mean(), 0.60],
                    range=["#BF8700", "White", "#0076BF"],
                ),
            ).legend(title="Recipiency Rate", format="%")
        )
        .project(type="albersUsa")
        .properties(width=600, height=300)
    )

    # Save chart
    return c7
