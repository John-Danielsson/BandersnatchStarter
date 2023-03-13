from altair import Chart
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    return Chart(
        data=df,
        mark='line',
        description='Data visualization of Bandersnatch data with an Altair Chart',
        title=f'x={x}, y={y}, target={target}'
    )
