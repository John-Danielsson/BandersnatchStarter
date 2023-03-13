from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    # Is the Chart object created using the correct syntax and parameters, including
    # the df, title, and mark_circle?
    chart = Chart(
        data=df,
        mark='circle',
        description='Data visualization of Bandersnatch data with an Altair Chart',
        title=f'{x} vs. {y} for {target}'
    )
    chart.mark_circle(size=100)
    # Are the correct encodings used for x, y, color, and tooltip?
    chart.encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    # Properties and configuration need to be added.
    # Is the properties dictionary complete, including four keys and their
    # corresponding values for width, height, background, and padding?
    chart.properties(
        width=200,
        height=200,
        background='ffffff',
        padding=10
    )
    # chart.configure(
    #
    # )
    return chart
