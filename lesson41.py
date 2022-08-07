###################################################################################
# - - - - - - Построение нейронных сетей с использованием Keras и TensorFlow - - - - #

# import pandas as pd
# import math
# import matplotlib.pyplot as plt
# # Импортируем метод классификации ближайшего соседа
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import BernoulliNB, GaussianNB
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.tree import plot_tree
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
#
#
# def Bayes(x_train, x_test, y_train):
#     classif = BernoulliNB()
#     # Обучение модели Наивного Байеса
#     classif.fit(x_train, y_train)
#     # Проверка модели на тестовой выборке
#     y_pred = classif.predict(x_test)
#
#     classif3 = GaussianNB()
#     # Обучение модели Наивного Байеса
#     classif3.fit(x_train, y_train)
#     # Проверка модели на тестовой выборке
#     y_pred3 = classif3.predict(x_test)
#
#     return y_pred, y_pred3
#
#
# def LogRegr(x_train, x_test, y_train):
#     # Создание модели логистической регрессии
#     classif = LogisticRegression(max_iter=10000)
#     # Обучение модели логистической регрессии
#     classif.fit(x_train, y_train)
#     # Проверка модели на тестовой выборке
#     y_pred = classif.predict(x_test)
#
#     return y_pred
#
#
# # функция расчета метрик качества
# def verif(y_test, y_pred):
#     print(accuracy_score(y_test, y_pred))
#     print(recall_score(y_test, y_pred))
#     print(precision_score(y_test, y_pred))
#     print(f1_score(y_test, y_pred))
#
#
# def des_tree(x_train, x_test, y_train):
#     # построение дерева решений с указанием параметров. (критерий разбиения, минимальное количество примеров для
#     # разбиения узлов, образования листьев)
#     classif = DecisionTreeClassifier(criterion='gini', min_samples_split=6, min_samples_leaf=6)
#     # обучение дерева решений
#     classif.fit(x_train, y_train)
#     # расчет на тестовой выборке
#     y_pred = classif.predict(x_test)
#     # построение дерева решений визуализация
#     fig = plt.figure(dpi=300, figsize=(20, 30))
#     plot_tree(classif, filled=True, feature_names=x_train.columns)
#     plt.show()
#
#     return y_pred
#
#
# def RandomForest(x_train, x_test, y_train):
#     # построение случайного леса с использованием параметров: количество деревьев в лесу, минимальное количество
#     # примеров для разбиения узлов, образования листьев
#     classif = RandomForestClassifier(n_estimators=5, random_state=1, min_samples_split=6, min_samples_leaf=6)
#     # обучение случайного леса
#     classif.fit(x_train, y_train)
#     # расчет на тестовой выборке
#     y_pred = classif.predict(x_test)
#
#     return y_pred
#
#
# def fill_nan(df, sex):
#     df_1_class_m_clear = df[(df.Sex == sex) & (df.Age) > 0]
#     mean_1_m = df_1_class_m_clear['Age'].mean()
#     df_1_class_m = df[(df.Sex == sex)]
#     df_1_class_m = df_1_class_m.fillna({'Age': mean_1_m})
#     print(df_1_class_m['Age'].isnull().sum())
#     return df_1_class_m
#
#
# # трансформация данных
# def transData(data):
#     # создание объекта кодирование категориальных данных
#     for column in data.columns:
#         if data[column].dtype != 'int64' and data[column].dtype != 'float64':
#             trans_data = LabelEncoder()
#     # Обучение кодировщика на обучающих данных
#         trans_data.fit(data[column])
#         data[column] = trans_data.transform(data[column])
#     # возвращаем закодированные данные данные
#         return trans_data.transform(data)
#
#
# df = pd.read_csv('train.csv')
# print(df.info())
#
# df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True, axis=1)
# print(df.info())
#
# df_1_class = df[df.Pclass == 1]
# df_2_class = df[df.Pclass == 2]
# df_3_class = df[df.Pclass == 3]
#
# print(df_1_class['Age'].isnull().sum())
# print(df_2_class['Age'].isnull().sum())
# print(df_3_class['Age'].isnull().sum())
#
# df_1_class_w = df_1_class[(df_1_class.Sex == 'female') & (pd.isna(df_1_class.Age)) == False]
#
# print(df_1_class_w['Age'].isnull().sum())
#
# # Заполнение поля возраст у мужчин и женщин по классам размещения
#
# df1 = fill_nan(df_1_class, 'male')
# df2 = fill_nan(df_1_class, 'female')
# df3 = fill_nan(df_2_class, 'male')
# df4 = fill_nan(df_2_class, 'female')
# df5 = fill_nan(df_3_class, 'male')
# df6 = fill_nan(df_3_class, 'female')
#
# train_data = pd.concat((df1, df2, df3, df4, df5, df6))
# train_data.dropna(inplace=True)
# print(train_data.info())
# print(train_data['Survived'].value_counts())
#
# test_data = pd.read_csv('test.csv')
# print(test_data.info())
# test_y = pd.read_csv('gender_submission.csv')
# print(test_y.info())
#
# test_data = pd.concat((test_data, test_y['Survived']), axis=1)
# print(test_data.info())
#
# test_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True, axis=1)
# print(test_data.info())
#
# df_1_class = test_data[test_data.Pclass == 1]
# df_2_class = test_data[test_data.Pclass == 2]
# df_3_class = test_data[test_data.Pclass == 3]
#
# df1 = fill_nan(df_1_class, 'male')
# df2 = fill_nan(df_1_class, 'female')
# df3 = fill_nan(df_2_class, 'male')
# df4 = fill_nan(df_2_class, 'female')
# df5 = fill_nan(df_3_class, 'male')
# df6 = fill_nan(df_3_class, 'female')
#
# test_data = pd.concat((df1, df2, df3, df4, df5, df6))
#
# test_data.dropna(inplace=True)
# print(test_data.info())
#
# train_data

###################################################################################
#

import pandas as pd
import math
import matplotlib.pyplot as plt
# Импортируем метод классификации ближайшего соседа
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, r2_score
import seaborn as sns


def lin_reg(x_train, x_test, y_train):
    reg = LinearRegression()
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_train)
    y_pred2 = reg.predict(x_test)

    print(reg.intercept_)  # b
    print(reg.coef_)  # m

    print('=====================')
    return y_pred


df = pd.read_csv('industrial_data.csv', delimiter=';', encoding='cp1251')
print(df)

sns.heatmap(df.corr(), annot=True, cbar=False)

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
