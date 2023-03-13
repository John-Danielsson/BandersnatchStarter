from altair import Chart, Tooltip, X, Y, Axis
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    # Is the Chart object created using the correct syntax and parameters, including
    # the df, title, and mark_circle?
    return Chart(
        data=df,
        description='Data visualization of Bandersnatch data with an Altair Chart',
        background='#cad9d4'
    ).properties(
        # Properties and configuration need to be added.
        # Is the properties dictionary complete, including four keys and their
        # corresponding values for width, height, background, and padding?
        title=f'{x} vs. {y} for {target}',
        width=400,
        height=300,
        padding=10,
    ).mark_circle(size=100).encode(
        # Are the correct encodings used for x, y, color, and tooltip?
        x=X(f'{x}:Q', axis=Axis(title=x, grid=False)),
        y=Y(f'{y}:Q', axis=Axis(title=y, grid=False)),
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).configure_view(
        strokeWidth=2,
        stroke='#000000'
    )
# .encode(
#     alt.X('gdpPercap:Q', scale=alt.Scale(type='log'),
#          axis=alt.Axis(title='GDP Per Capita', grid=False)),
#     alt.Y('lifeExp:Q', scale=alt.Scale(zero=False),
#          axis=alt.Axis(title='Life Expectancy', grid=False)),
#      color='continent:N',
#      opacity=alt.value(0.5)
# )
