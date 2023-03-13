from altair import Chart
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    chart = Chart(
        data=df,
        mark='line',
        description='Data visualization of Bandersnatch data with an Altair Chart',
        title=f'x={x}, y={y}, target={target}'
    )
    chart.properties(
        width=200,
        height=200,
        background='ffffff',
        padding=10
    )
    return chart
