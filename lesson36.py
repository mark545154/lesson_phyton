###################################################################################
# - - - - - Машинное обучение с использованием Scikit-learn - - - - - - #
# Автомобили – набор данных о принятии решения о покупке
# Набор данных о решении о покупке, показывающий, купил ли клиент автомобиль.
#
# О наборе данных
# Этот набор данных содержит сведения о 1000 клиентов, которые намереваются купить автомобиль,
# с учетом их годовой заработной платы.
# Столбцы:
# ID пользователя
# Пол
# Возраст
# Годовой оклад
# Решение о покупке (Нет = 0; Да = 1)
# Загрузить данные. Проверить качество.
# Разделить данные на тестовую и обучающую выборку
# Построить модель классификации.

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

# Создание датафрейма (объект pandas см документацию) из файла csv
df = pd.read_csv('car_data.csv')
# Вывод верхних n строк (по умолчанию 5), параметр в скобках - кол-во строк
print(type(df.head(10)))
print(type(df['Age']))

# вывод названий столбцов датафрейма в форме списка python
# print(df.columns)
# Вывод
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df['AnnualSalary'].mean())

# print(df.duplicated().sum())  # Проверяем на дубликаты и какое их кол-во

dupl = df.duplicated(subset=(df.columns[1:]))
df.drop_duplicates(subset=(df.columns[1:-1]), inplace=True)

dupl = df.duplicated(subset=(['Gender', 'Age', 'AnnualSalary', 'Purchased']))  # Проверка на дубликаты - противоречия
df.drop_duplicates(subset=(['Gender', 'Age', 'AnnualSalary', 'Purchased']), inplace=True)  # inplace указывается
# обязательно, перезаписывает df
df.reset_index(inplace=True, drop=True)  # делаем reset_index чтобы обновить индексы в df, drop обновляет индексы

dupl = df.duplicated(subset=(['Gender', 'Age', 'AnnualSalary']))
dupl = dupl[dupl == True]
print(dupl)


# print(df.iloc()[506])
# print(df[(df['Gender'] == 'Male') & (df['Age'] == 40) & (df['AnnualSalary'] == 72500)])

# print(df.isnull().sum())  # Проверяем на пропуски
print(df.info())

trans = preprocessing.LabelEncoder()
trans.fit(df['Gender'])
df['Gender'] = trans.transform(df['Gender'])
print(df['Gender'].unique())

scaller = MinMaxScaler()
scaller.fit(df[['Age']])
df['Age'] = scaller.transform(df[['Age']])

scaller.fit(df[['AnnualSalary']])
df['AnnualSalary'] = scaller.transform(df[['AnnualSalary']])

print(df)

train_x, test_x, train_y, test_y = train_test_split(df[df.columns[1:-1]], df[df.columns[-1]], train_size=0.8, random_state=7)  # Создаём тестовую и обучающую выборку

print(train_y.value_counts())
print(test_y.value_counts())
classif = KNeighborsClassifier(n_neighbors=5)  # Создаём пустую модель ближайшего соседа
classif.fit(train_x, train_y)

y_pred = classif.predict(test_x)
print(len(test_y))
print(accuracy_score(test_y, y_pred))

###################################################################################
# Код Виктории Михайловны с коментами

# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn import preprocessing
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import MinMaxScaler
#
#
#
# #Создание датафрейма (объект pandas см документацию) из файла csv
# df = pd.read_csv('car_data.csv')
# #Вывод верхних n строк (по умолчанию 5), параметр в скобках - количество строк
# print(df.head(10))
# print(type(df['Age']))
# #вывод названий столбцов датафрема в форме списка python
# print(df.columns)
# #Вывод нижних n строк (по умолчанию 5), параметр в скобках - количество строк
# print(df.tail())
# #Вывод описательной статистики
# print(df.describe())
# #Расчет среднего
# print(df['AnnualSalary'].mean())
# #Проверка дубликатов, subset ограничивает столбцы, смотри методичку по очистке данных
# dupl = df.duplicated(subset=(df.columns[1:]))
# #Удаляем дубликаты
# df.drop_duplicates(subset=(df.columns[1:-1]), inplace=True)
# #Обновляем индексы
# df.reset_index(inplace = True, drop=True)# df = df.reset_index(drop=True)
#
# dupl = df.duplicated(subset=(['Gender', 'Age', 'AnnualSalary']))
# #Выбираем строки с дубликатами (фильтр по Series)
# dupl = dupl[dupl==True]
#
# print(df)
# print(dupl)
# #Вывод и обращение к строке DataFrame по индексу (номеру строки)
# print(df.iloc()[506])
# #Выбор строк из DataFrame по условию (фильтр)
# print(df[(df['Gender'] == 'Male') & (df['Age']==40)& (df['AnnualSalary']== 72500)])
#
# #Кодирование нечисловых данных в числовые
# trans = preprocessing.LabelEncoder()
# trans.fit(df['Gender'])
# df['Gender'] = trans.transform(df['Gender'])
# print(df['Gender'].unique())
#
# #Нормализация данных
# scaller = MinMaxScaler()
# scaller.fit(df[['Age']])
# df['Age'] = scaller.transform(df[['Age']])
# #Нормализация данных
# scaller.fit(df[['AnnualSalary']])
# df['AnnualSalary'] = scaller.transform(df[['AnnualSalary']])
#
# print(df)
# #Пазбиение на обучающую и тестовую выборки (подробнее в предыдущей лекуии)
# train_x, test_x, train_y, test_y = train_test_split(df[df.columns[1:-1]], df[df.columns[-1]],
#                                                     train_size = 0.8, random_state = 7)
#
#
# print(train_y.value_counts())
# print(test_y.value_counts())
# #Создание модели ближайшего соседа (n_neighbors - количнство соседей)
# classif = KNeighborsClassifier(n_neighbors=5)
# #Обучение модели
# classif.fit(train_x, train_y)
# #Подстановка в обученную модель тестовых данных
# y_pred = classif.predict(test_x)
# print(len(test_y))
# #Оценка точности модели классификации (отношение верно распознанных к общему количеству строк в тестовой выборке)
# print(accuracy_score(test_y, y_pred))

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
