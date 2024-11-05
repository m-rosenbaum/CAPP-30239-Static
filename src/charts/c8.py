import altair as alt


# Ref for kernel density: https://altair-viz.github.io/user_guide/transform/density.html
# Ref for stacking: https://altair-viz.github.io/gallery/ridgeline_plot.html
def c8(st) -> alt.Chart:
    """
    Writes a lasagna graph to show radical break on key states for recipiency
    with the pandemic.

    Input:
        file (pl.DataFrame): File with federal unemployment

    Returns (Chart): Chart object
    """
    # Establish scaling parameters
    step = 30
    overlap = 1
    st_mean = st["rt_recip"].mean()

    c8 = (
        alt.Chart(st)
        .transform_density(
            "rt_recip", groupby=["st"], as_=["rt_recip", "density"], extent=[0, 1]
        )
        # Below doesn't work
        # .transform_aggregate(mean_rt_recip="mean(rt_recip)", groupby=["st"])
        .mark_area(
            # Color example from: https://altair-viz.github.io/user_guide/marks/area.html
            line={
                "color": "#0076BF",
            },
            color=alt.Gradient(
                gradient="linear",
                stops=[
                    alt.GradientStop(color="#0076BF50", offset=0),
                    alt.GradientStop(color="#0076BF", offset=1),
                ],
                # Make gradient vertical
                x1=1,
                x2=1,
                y1=1,
                y2=0,
            ),
        )
        .encode(
            alt.X("rt_recip:Q", scale=alt.Scale(domainMin=0, domainMax=1))
            .title("Recipency Rate")
            .axis(format="%"),
            alt.Y("density:Q").axis(None).scale(range=[step, -step * overlap]),
            # alt.Color("mean_rt_recip:Q", scale=alt.Scale(scheme="blues")),
        )
        .properties(height=30)  # Control each subplot height
        .facet(
            row=alt.Row("st:N").title(None).header(labelAngle=0, labelAlign="left"),
            spacing=0,
        )
        .properties(
            title=alt.Title(
                "Recipiency rates have different ranges in the largest states",
                subtitle="Density of recipiency rates between 2006-2024",
            ),
            bounds="full",
        )
        .configure_facet(spacing=0)
    )

    # rule = (
    #    alt.Chart()
    #    .mark_rule(color="#203440", strokeWidth=1)
    #    .encode(x=alt.X(datum=st_mean))
    # )

    return c8
