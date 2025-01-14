###################################################################################
# - - - - - Построение нейронных сетей с использованием Keras и TensorFlow (лекция) - - - - #

# Андр семплинг!!! (уравнение 0 и единиц)

import pandas as pd

df = pd.read_csv('bank-marketing.csv')
print(df.info())

data0 = df[df['response'] == 0]
data1 = df[df['response'] == 1]

num0 = len(data0)
num1 = len(data1)
print(num0, num1)

new_data0 = data0.sample(num1, random_state=1)
print(len(new_data0))

df = pd.concat((data1, new_data0))
print(df['response'].value_counts())


###################################################################################
#
# НОРМАЛИЗАЦИЯ ДАННЫХ (ПРИВЕДЕНИЕ К ЗНАЧЕНИЮ ОТ 0 ДО 1)

# def normData (data):
#     data = pd.DataFrame(data)
#     scaler = MinMaxScaler()
#     scaler.fit(data)
#     return scaler.transform(data)

###################################################################################
#
# ТРАНСФОРМАЦИЯ СТРОКОВЫХ ДАННЫХ В ЧИСЛОВОЙ РЯД
# def transData(data):
#     trans_data = LabelEncoder()
#     trans_data.fit(data)
#
#     return trans_data.transform(data)

