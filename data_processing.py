import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

# import data
df = pd.read_csv('processed.csv')

# drop unnecessary columns
df.drop(labels="index", axis=1, inplace=True)

# replace Y/N with 1/0
df['neo'] = df['neo'].map({'Y': 1, 'N': 0})
df['pha'] = df['pha'].map({'Y': 1, 'N': 0})

# type cast data
df = df.astype(float)

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