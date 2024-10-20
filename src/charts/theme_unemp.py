# Create custom theme:
def unemp_theme():
    return {
        "config": {
            # Fix grid lines
            "view": {"stroke": "transparent", "width": 800, "heigh": 300},
            "axis": {
                "labelFont": "Helvetica",
                "titleFont": "Helvetica",  # Set font to Helvetica
            },
            "axisY": {
                "domain": False,
                "ticks": True,
                "grid": True,
                "gridDash": [3, 3],
                "tickColor": "#33333320",  # 20% opacity
                "gridColor": "#33333320",
            },
            "axisX": {"grid": False},
            "title": {"font": "Helvetica"},
            "legend": {
                "labelFont": "Helvetica",
                "titleFont": "Helvetica",
            },
            # Set up a custom palette, constant saturation
            "range": {
                "category": [
                    "#0076BF",  # DOL Strong Blue
                    "#BF4E00",  # Split Complimentary Orange
                    "#6B4D23",  # Complimentary Brown
                    "#BF8700",  # Split Complimentary Yellow
                    "#203440",  # "Darkened Blue"
                ]
            },
            "title": {
                "anchor": "start",
                "orient": "top",
                "offset": 20,
            },
        }
    }
