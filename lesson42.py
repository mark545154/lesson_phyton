###################################################################################
# - - - - - - Построение нейронных сетей с использованием Keras и TensorFlow - - - - #

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('marketing_campaign.csv', delimiter='\t')
print(df.info())

df = df.dropna()
df.reset_index(inplace=True, drop=True)


def transData(data):
    for column in data.columns:
        if data[column].dtype != 'int64' and data[column].dtype != 'float64':
            trans_data = LabelEncoder()
            # Обучение кодировщика на обучающих данных
            trans_data.fit(data[column])
            data[column] = trans_data.transform(data[column])
    # возвращаем закодированные данные данные
    return data


def normData(data):
    for column in data.columns:
        if abs(data[column].max()) > 1:
            scaler = MinMaxScaler()
            # обучение на данных
            scaler.fit(data[[column]])
            data[column] = scaler.transform(data[[column]])
    # возвращаем нормализованные данные
    return data


df = transData(df)

df = normData(df)
print(df)
silhouette_list = []
for number in range(2, 10):
    cluster = KMeans(n_clusters=number, random_state=0)
    cluster.fit(df)

    silhouette_list.append(silhouette_score(df, cluster.labels_))

plt.plot(range(2, 10), silhouette_list)
plt.show()

###################################################################################
#

###################################################################################
#

###################################################################################
#

###################################################################################
#

###################################################################################
#

###################################################################################
#

###################################################################################
#

###################################################################################
#

###################################################################################
#

###################################################################################
#
