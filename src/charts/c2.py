import altair as alt


def c2(elig, ic, claimed):
    """
    Creates a series of Chart elements
    """
    # Creates eligibility base layer
    c2_elig = (
        alt.Chart(
            elig,
            title=alt.Title(
                "Filing for UI isn't something you do just once, it's something you have to do every week",
                subtitle="Individuals first must be eligible for UI, then file their initial claim, then file each week",
            ),
        )
        .mark_point(size=100, filled=True, color="#33333340")
        .encode(
            alt.X("elig")
            .title("Week of Unemployment")
            .axis(domain=False, ticks=True, values=range(1, 27)),
            alt.Y("y")
            .title(None)
            .axis(
                domain=False,
                ticks=False,
                grid=False,
                labels=True,
                values=[4, 2, 3, 1],
                labelPadding=10,  # Adding padding for the manual changes
            ),
        )
    )

    # Creates initial claim layers
    c2_ic = (
        alt.Chart(ic).mark_point(size=100, filled=False).encode(alt.X("ic"), alt.Y("y"))
    )

    # Creates filled in claimed information
    c2_claimed = (
        alt.Chart(claimed)
        .mark_point(size=100, filled=True)
        .encode(alt.X("claimed"), alt.Y("y"))
    )

    ## Annotations
    # Annotation 1
    # Ref: https://altair-viz.github.io/gallery/line_chart_with_arrows.html
    person_a = alt.layer(
        # Arrow line
        alt.Chart()
        .mark_line(size=1)
        .encode(
            x=alt.datum(2),
            y=alt.datum(3.8),
            x2=alt.datum(3),
            y2=alt.datum(3.5),
            color=alt.ColorValue("#33333380"),
        ),
        # Arrow head
        alt.Chart()
        .mark_point(shape="triangle", filled=True, fillOpacity=1)
        .encode(
            x=alt.datum(3),
            y=alt.datum(3.5),
            angle=alt.AngleValue(-30),
            size=alt.SizeValue(50),
            color=alt.ColorValue("#33333380"),
        ),
        # Text
        alt.Chart()
        .mark_text(size=10, align="left", baseline="middle")
        .encode(
            x=alt.datum(3.3),
            y=alt.datum(3.5),
            text=alt.datum(
                "Abigail files weekly and receives benefits each week until they exhaust their benefits after 26 weeks"
            ),
        ),
    )

    # Annotation 2
    person_b = alt.layer(
        # Arrow line
        alt.Chart()
        .mark_line(size=1)
        .encode(
            x=alt.datum(12),
            y=alt.datum(2.8),
            x2=alt.datum(13),
            y2=alt.datum(2.5),
            color=alt.ColorValue("#33333380"),
        ),
        # Arrow head
        alt.Chart()
        .mark_point(shape="triangle", filled=True, fillOpacity=1)
        .encode(
            x=alt.datum(13),
            y=alt.datum(2.5),
            angle=alt.AngleValue(-30),
            size=alt.SizeValue(50),
            color=alt.ColorValue("#33333380"),
        ),
        # Text
        alt.Chart()
        .mark_text(size=10, align="left", baseline="middle")
        .encode(
            x=alt.datum(13.3),
            y=alt.datum(2.5),
            text=alt.datum(
                "Bryan lives in Florida, which only provides 12 weeks of benefits"
            ),
        ),
    )

    # Annotation 3
    person_c = alt.layer(
        # Arrow line
        alt.Chart()
        .mark_line(size=1)
        .encode(
            x=alt.datum(4),
            y=alt.datum(1.8),
            x2=alt.datum(4.7),
            y2=alt.datum(1.5),
            color=alt.ColorValue("#33333380"),
        ),
        # Arrow head
        alt.Chart()
        .mark_point(shape="triangle", filled=True, fillOpacity=1)
        .encode(
            x=alt.datum(4.7),
            y=alt.datum(1.5),
            angle=alt.AngleValue(-30),
            size=alt.SizeValue(50),
            color=alt.ColorValue("#33333380"),
        ),
        # Text
        alt.Chart()
        .mark_text(size=10, align="left", baseline="middle")
        .encode(
            x=alt.datum(5.1),
            y=alt.datum(1.5),
            text=alt.datum(
                "Carlos doesn't file their weekly certification week 4, and therefore doesn't receve benefits"
            ),
        ),
    )

    # Annotation 4
    person_d = alt.layer(
        # Arrow line
        alt.Chart()
        .mark_line(size=1)
        .encode(
            x=alt.datum(1),
            y=alt.datum(0.8),
            x2=alt.datum(1.6),
            y2=alt.datum(0.5),
            color=alt.ColorValue("#33333380"),
        ),
        # Arrow head
        alt.Chart()
        .mark_point(shape="triangle", filled=True, fillOpacity=1)
        .encode(
            x=alt.datum(1.6),
            y=alt.datum(0.5),
            angle=alt.AngleValue(-30),
            size=alt.SizeValue(50),
            color=alt.ColorValue("#33333380"),
        ),
        # Text
        alt.Chart()
        .mark_text(size=10, align="left", baseline="middle")
        .encode(
            x=alt.datum(2.0),
            y=alt.datum(0.5),
            text=alt.datum("Divya never files an initial claim"),
        ),
    )

    # Combine chart with preferred ordering
    c2 = c2_elig + c2_ic + c2_claimed + person_a + person_b + person_c + person_d

    # Return combined chart
    return c2
