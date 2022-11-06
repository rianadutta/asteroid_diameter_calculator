import pandas as pd
import numpy as np
from scipy import stats

# import data
df = pd.read_csv('processed.csv')

# drop unnecessary columns
df.drop(labels=["index","pha"], axis=1, inplace=True)

# replace Y/N with 1/0
df['neo'] = df['neo'].map({'Y': 1, 'N': 0})

# type cast data
df = df.astype(float)

# remove outliers
for column in df:
    if column not in ["orbit_condition_code","neo"]:
        df=df[(np.abs(stats.zscore(df[column])) < 3)]

# normalize data
def min_max_scaling(column):
    return (column-column.min())/(column.max()-column.min())
for column in df.columns:
    if column != 'diameter':
        df[column]=min_max_scaling(df[column])

# shuffle dataframe
df = df.sample(frac = 1)

# split dataframe into train and test
split_index = int(df.shape[0] * 0.8)
df_train = df.iloc[:split_index]
df_test = df.iloc[split_index:]

# split train and test into X and Y
Y_train = df_train['diameter']
Y_test = df_test['diameter']
X_train = df_train.drop(labels='diameter',axis=1)
X_test = df_test.drop(labels='diameter',axis=1)