# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:17:34 2022

@author: lesna
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
import seaborn as sns
from sklearn.metrics import mean_absolute_percentage_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from joblib import dump, load
#метод линейной регрессии
def lin_reg (x_train, x_test, y_train):
 
    reg = LinearRegression()
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    y_pred2 = reg.predict(x_train)
    print(r2_score(y_train, y_pred2))
    

    print(reg.intercept_) # b
    print(reg.coef_) #m
    dump(reg, 'линрегрессия.joblib')
 

    return  y_pred 
#метод дерева решений
def des_tree (x_train, x_test, y_train):
    
    reg = DecisionTreeRegressor()
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    y_pred2 = reg.predict(x_train)
    print(r2_score(y_train, y_pred2))
    dump(reg, 'дерево.joblib')

    return y_pred

def verif (y_test, y_pred):
    
    print(mean_absolute_percentage_error(y_test, y_pred))
    
def normData (data):
#создание объекта нормализации
    for column in data.columns:
        scaler = MinMaxScaler()
        try:
            scaler.fit(data[column])
        except ValueError:
            continue
        #обучение на данных
        
    #возвращаем нормализованные данные
        data[column] = scaler.transform(data) 
    return data
#метод создания нейронной сети
def NN (x_train, x_test, y_train):
    reg = MLPRegressor(hidden_layer_sizes=(100,), activation = 'relu', 
                       solver = 'adam', random_state=18, max_iter = 50,
                       batch_size=11)
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    y_pred2 = reg.predict(x_train)
    print(r2_score(y_train, y_pred2))
    dump(reg, 'нейроннаясеть.joblib')

    return y_pred


    
df = pd.read_csv('industrial_data.csv', delimiter = ';', encoding = 'cp1251')
print(df)
sns.heatmap(df.corr(), annot = True, cbar = False)
#Выбираем X
X = df[['M2', 'VVP']]
#выбираем y
y = df[['LESMAT']]
#обрабатываем данные, как упорядоченные данные, поэтому делим на тестовую и обучающую в определенном порядке
x_train = X.iloc()[:-2]
x_test = X.iloc()[-2:]

y_train = y.iloc()[:-2]
y_test = y.iloc()[-2:]
#вызоы метода линейной регрессии
y_pred_reg = lin_reg (x_train, x_test, y_train)
verif (y_test, y_pred_reg)
print('==================')
#вызов метода дерева решений
y_pred_dec = des_tree(x_train, x_test, y_train)
verif (y_test, y_pred_dec)
print('==================')
#нормализация данных
X = normData(X)
y = normData(y)
x_train = X.iloc()[:-2]
x_test = X.iloc()[-2:]

y_train = y.iloc()[:-2]
y_test = y.iloc()[-2:]
#вызов нейронной сети
y_pred_NN = NN (x_train, x_test, y_train)
verif (y_test, y_pred_NN)

pred = pd.read_csv('test.csv', delimiter = ';', encoding = 'cp1251')
print(pred)

x = pred[['M2', 'VVP']]
x_norm = normData(x)
#загрузка модели из файлв
model1 = load('линрегрессия.joblib')
#Построение прогноза
forecast1 = model1.predict(x)
#Построение прогноза
print(forecast1)
#загрузка модели из файлв
model2 = load('дерево.joblib')
#Построение прогноза
forecast2 = model2.predict(x)
print(forecast2)

#загрузка модели из файлв
model3 = load('нейроннаясеть.joblib')
#Построение прогноза
forecast3 = model3.predict(x_norm)
print(forecast3)

