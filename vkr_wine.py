import pandas as pd
# Импортируем метод классификации ближайшего соседа
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

df = pd.read_csv('vkr_winequality-red.csv', delimiter=',')
# print(df)
print(df.info())
# print(df.head(10))
# print(df.iloc()[0])
# print(df.columns)
# print(df.tail())
print(df.describe())
# print(df['alcohol'].mean())
# print(df['alcohol'].unique())
print(df.duplicated().sum())








