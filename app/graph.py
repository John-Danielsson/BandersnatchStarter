from altair import Chart, Tooltip, X, Y, Axis
from pandas import DataFrame


"""
Returns a chart displaying a scatter plot showing the
relationship between 3 variables x, y, and target.
The 3rd variable, target is represented by the color
of the dot it is associated with, which represents
an individual monster.
"""


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    return Chart(
        data=df,
        description='Data visualization of Bandersnatch data with an Altair Chart',
    ).properties(
        title=f'{x} vs. {y} for {target}',
        width=400,
        height=300,
        padding=10,
        background='#000000'
    ).mark_circle(size=100).encode(
        x=X(f'{x}:Q', axis=Axis(title=x, grid=False)),
        y=Y(f'{y}:Q', axis=Axis(title=y, grid=False)),
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).configure_view(
        strokeWidth=2,
        stroke='#c0ebde'
    ).configure_axis(
        labelColor='#c0ebde',
        titleColor='#c0ebde'
    ).configure_legend(
        labelColor='#c0ebde',
        titleColor='#c0ebde'
    ).configure_title(
        color='#c0ebde'
    )
