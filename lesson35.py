###################################################################################
# - - - - - Машинное обучение с использованием Scikit-learn - - - - - #

# # Евклидово расстояние между двумя объектами
# def dist(movie1, movie2):
#     diff = 0
#     for index in range(len(movie1)):
#         diff += (movie1[index] - movie2[index]) ** 2
#     return diff ** 0.5
#
#
# # Нормализация данных (привидение данных к интервалу от 0 до 1)
# def normalization(data):
#     result = []
#     for item in data:
#         item = (item - min(data)) / (max(data) - min(data))
#         result.append(item)
#     return result
#
#
# # Обучающая выборка
# star_wars = [1977, 125, 11000000]
# raiders_of_the_Lost_Ark = [1981, 105, 18000000]
# mean_girls = [2004, 97, 17000000]
# # Метки классов
# y = [0, 1, 1]
#
# # Тестовая выборка
# Avatar = [2009, 162, 237000000]
#
# # Подготовка данных к нормализации (объединяем однородные группы, т.е. годы с годами, длительность с длительностью и
# # т.д.)
# years = [star_wars[0], raiders_of_the_Lost_Ark[0], mean_girls[0], Avatar[0]]
# time = [star_wars[1], raiders_of_the_Lost_Ark[1], mean_girls[1], Avatar[1]]
# budget = [star_wars[2], raiders_of_the_Lost_Ark[2], mean_girls[2], Avatar[2]]
#
# # Нормализация данных
# years_norm = normalization(years)
# time_norm = normalization(time)
# budget_norm = normalization(budget)
#
# star_wars = [years_norm[0], time_norm[0], budget_norm[0]]
# raiders_of_the_Lost_Ark = [years_norm[1], time_norm[1], budget_norm[1]]
# mean_girls = [years_norm[2], time_norm[2], budget_norm[2]]
# Avatar = [years_norm[3], time_norm[3], budget_norm[3]]
#
# # print(years_norm)
# # print(time_norm)
# # print(budget_norm)
# # print('Звездные войны и ковчег', dist(star_wars, raiders_of_the_Lost_Ark))
# # print('Звездные войны и дрянные девчонки', dist(star_wars, mean_girls))
# # print('ковчег и дряные девчонки', dist(raiders_of_the_Lost_Ark, mean_girls))
#
# print('Аватар и звездные войны', dist(star_wars, Avatar))
# print('Аватар и дрянные девчонки', dist(mean_girls, Avatar))
# print('Аватар и ковчег', dist(raiders_of_the_Lost_Ark, Avatar))

###################################################################################
#

import pandas as pd
# Импортируем метод классификации ближайшего соседа
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

df = pd.read_csv('glassKNN.csv', delimiter=';')
print(df)
print(df.info())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

print(df['Type'].value_counts())
x_train, x_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]],
                                                    test_size=0.8, random_state=2)
# Создание и конфигурирование модели ближайшего соседа (n_neighbors - количество соседей)
classif = KNeighborsClassifier(n_neighbors=4)
# Обучение модели методом ближайшего соседа (расчет расстояний) обучающая выборка
classif.fit(x_train, y_train)
# Проверка модели на тестовой выборке
y_pred = classif.predict(x_test)
# Результат расчета на тестовой выборке
y_pred

# Вывод тестовой выборки для просмотра и сравнения с результатом расчета
(np.array(y_test)).reshape(1, -1)

# Расчет метрики точности классификации accuracy (отношение верно соотнесенных примеров с общим колиеством объектов в
# тестовой выборке)
accuracy_score(y_test, y_pred)


