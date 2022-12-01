# %%
import numpy as np
import pandera as pa
import pandas as pd

df = pd.read_csv('ships.csv')
df
# %%

schema = pa.DataFrameSchema({
    'name': pa.Column(pa.String),
    'lat': pa.Column(pa.Float),
    'lng': pa.Column(pa.Float),
})

schema.validate(df)

# %%
new_schema = pa.DataFrameSchema({
    'name': pa.Column(pa.String),
    'lat': pa.Column(pa.Float, nullable=True),
    'lng': pa.Column(pa.Float, nullable=True),
})

new_schema.validate(df)
