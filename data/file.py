import pandas as pd


from settings import PROPERTIES

raw_data = pd.read_csv(
    PROPERTIES.relative_path, 
    dtype=PROPERTIES.datatype, 
    parse_dates=PROPERTIES.parse_dates,
    dayfirst=True,
    thousands=',',
    decimal='.'
)

