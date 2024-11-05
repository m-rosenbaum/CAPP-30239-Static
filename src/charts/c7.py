import altair as alt
import polars as pl


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
    # Data processing
    st = st.filter(filt)
    fed = fed.filter(filt)
    st = st.drop("date")  # don't need date
    fed = fed.drop("date")

    # Ref from: https://altair-viz.github.io/gallery/choropleth.html
    c7 = (
        alt.Chart(
            geo,
            title=alt.Title(
                "Southern states have below average recipiency",
                subtitle="Average recipiency in 2019",
            ),
        )
        .mark_geoshape()
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(st, "id", ["rt_recip"]),
        )
        .encode(
            alt.Color(
                "rt_recip:Q",
                scale=alt.Scale(
                    domain=[0, 0.60],  # fed.filter(filt)["rt_recip"].mean(),
                    range=["#33333310", "#0076BF"],
                ),
            ).legend(title="Recipiency Rate", format="%")
        )
        .project(type="albersUsa")
        .properties(width=800, height=400)
    )

    # Save chart
    return c7
