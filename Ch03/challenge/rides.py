# %%
import pandas as pd

df = pd.read_csv('rides.csv')
df
# %%
# Find out all the rows that have bad values
# - Missing values are not allowed
# - A plate must be a combination of at least 3 upper case letters or digits
# - Distance much be bigger than 0

# %%
df[df.isnull().any(axis=1)]

#%% 
import numpy as np
df.plate = df.plate.str.strip()
mask = df.plate == ''
df.loc[mask, 'plate'] = np.nan
df

#%% 
df.duplicated()

#%% 
df.dtypes

#%%
df_new = df.dropna(axis=0)
df_new

# %%
dist = df_new.distance
z_score = (dist - dist.mean())/dist.std()
bad_dist = dist[z_score.abs() > 2]
bad_dist
# %%
df_new.loc[bad_dist.index]
#%% 
import pandera as pa
schema = pa.DataFrameSchema({
    'name': pa.Column(pa.String),
    'distance': pa.Column(
        pa.Float,
        nullable=True,
        checks=pa.Check(
            lambda v: v > 0,
            element_wise=True,
        ),
    ),
    'plate': pa.Column(
        pa.String,
        nullable=True,
        checks=pa.Check(
            lambda v: sum(1 for c in v
                if c.isupper() or
                    c.isdigit()) > 0,
            element_wise=True,
        ),
    ),
})

schema.validate(df_new)
