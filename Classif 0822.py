# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:12:26 2022

@author: lesna
"""

import pandas as pd
import matplotlib.pyplot as plt
# Импортируем метод классификации ближайшего соседа
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import pickle  # библиотека загрузки объектов в файл
from joblib import dump, load


# метод соседа
def neighbor(x_train, x_test, y_train, n):
    # classif - объект, который хранит модель
    classif = KNeighborsClassifier(n_neighbors=n)
    classif.fit(x_train, y_train)
    y_pred = classif.predict(x_test)
    # сериализация модели в файл (объект в словарь) и запись в файл с библиотекой pickle
    with open('data.pickle', 'wb') as f:
        pickle.dump(classif, f)
    # сериализация модели в файл (объект в словарь) и запись в файл с библиотекой joblib
    dump(classif, 'neighbor.joblib')

    return y_pred


def Bayes(x_train, x_test, y_train):
    classif = BernoulliNB()
    # Обучение модели Наивного Байеса
    classif.fit(x_train, y_train)
    # Проверка модели на тестовой выборке
    y_pred = classif.predict(x_test)

    classif3 = GaussianNB()
    # Обучение модели Наивного Байеса
    classif3.fit(x_train, y_train)
    # Проверка модели на тестовой выборке
    y_pred3 = classif3.predict(x_test)

    return y_pred, y_pred3


def LogRegr(x_train, x_test, y_train):
    # Создание модели логистической регрессии
    classif = LogisticRegression(max_iter=10000)
    # Обучение модели логистической регрессии
    classif.fit(x_train, y_train)
    # Проверка модели на тестовой выборке
    y_pred = classif.predict(x_test)

    return y_pred


# функция расчета метрик качества
def verif(y_test, y_pred):
    print(accuracy_score(y_test, y_pred))
    print(recall_score(y_test, y_pred))
    print(precision_score(y_test, y_pred))
    print(f1_score(y_test, y_pred))


def des_tree(x_train, x_test, y_train):
    # построение дерева решений с указанием параметров. (критерий разбиения, минимальное количество примеров для разбиения узлов, образования листьев)
    classif = DecisionTreeClassifier(criterion='gini', min_samples_split=6, min_samples_leaf=6)
    # обучение дерева решений
    classif.fit(x_train, y_train)
    # расчет на тестовой выборке
    y_pred = classif.predict(x_test)
    # построение дерева решений визуализация
    fig = plt.figure(dpi=300, figsize=(20, 30))
    plot_tree(classif, filled=True, feature_names=x_train.columns)
    plt.show()

    return y_pred


def RandomForest(x_train, x_test, y_train):
    # построение случайного леса с использованием параметров: количество деревьев в лесу, минимальное количество примеров для разбиения узлов, образования листьев
    classif = RandomForestClassifier(n_estimators=5, random_state=1, min_samples_split=6, min_samples_leaf=6)
    # обучение случайного леса
    classif.fit(x_train, y_train)
    # расчет на тестовой выборке
    y_pred = classif.predict(x_test)

    return y_pred


# загрузка файла
df = pd.read_csv('glassKNN.csv', delimiter=';')
print(df.info())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print(df['Type'].value_counts())
x_train, x_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]],
                                                    train_size=0.8, random_state=10)
# вызов функцийразных моделей на одних и тех же данных
# Вызов функции ближайшего соседа
print('Ближайший сосед')
verif(y_test, neighbor(x_train, x_test, y_train, 5))
print('======================')
# Вызов функции наивного Байеса
print('Байес')
y1, y2 = Bayes(x_train, x_test, y_train)
verif(y_test, y1)
print('============')
verif(y_test, y2)
print('============')
# Вызов функции логистической регрессии
print('Лог регрессия')
verif(y_test, LogRegr(x_train, x_test, y_train))
print('============')
print('Дерево решений')
verif(y_test, des_tree(x_train, x_test, y_train))
print('============')
print('Случайный лес')
verif(y_test, RandomForest(x_train, x_test, y_train))
# загрузка обученной модели из файла библиотека pickle
s = open('data.pickle', 'rb')
model = pickle.load(s)
# расчет с использованием обученной модели, загруженной из файла
model.predict(x_test)

# загрузка обученной модели из файла библиотека joblib
model2 = load('neighbor.joblib')
# расчет с использованием обученной модели, загруженной из файла
model2.predict(x_test)
