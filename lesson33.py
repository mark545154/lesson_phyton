###################################################################################
# - - - - Машинное обучение с использованием Scikit-learn - - - - - #

# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.metrics import mean_absolute_percentage_error  # ошибка MAPE
# import numpy as np
#
# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156]
#
#
# def data_prepare(data, shape):
#     data = np.reshape(np.array(data), shape)
#     return data
#
#
# def lin_reg(x, y, x_test, y_test):
#     regr = LinearRegression()
#     regr.fit(x, y)
#     y_pred = regr.predict(x)
#     y_pred2 = regr.predict(x_test)
#     # y_pred = [float(regr.coef_)*month[i]+float(regr.intercept_) for i in range(len(month))]
#     print(regr.coef_)  # m
#     print(regr.intercept_)  # b
#     print(r2_score(y, y_pred))
#     print(mean_absolute_percentage_error(np.array(y_test), y_pred2))
#
#     return y_pred, y_pred2
#
#
# y1, y2 = lin_reg(data_prepare(month, (-1, 1)), np.array(revenue),
#                  data_prepare([12], (-1, 1)), [184])
#
# print(y2)
# plt.plot(month, revenue, 'o')
# plt.plot(month, y1)
# plt.plot(12, y2, 'o')
# plt.show()

###################################################################################
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.model_selection import train_test_split  # Делит нашу выборку на тестовую и обучающую
#
#
# df = pd.read_csv('Dannye.csv', delimiter=';', encoding='cp1251')
# print(df.info())
#
#
# sns.heatmap(df.corr(), annot=True, cbar=False)  # метод корреляции, annot=True выводит цифры на графике
# plt.show()
#
# def lin_reg(x, y):
#     regr = LinearRegression()
#     regr.fit(x, y)
#     y_pred = regr.predict(x)
#     print(regr.coef_)  # m
#     print(regr.intercept_)  # b
#     print(r2_score(y, y_pred))
#
#     return y_pred
#
# x1 = pd.DataFrame(df['X1'])  # Показываем что наш объект DataFrame, и после трансформации передаем как переменную в регрессию fit
# # reg = LinearRegression()
# # reg.fit(x, df['Y'])
# # print(reg.coef_, reg.intercept_)
# # y_pred = reg.predict(x)
# # print(r2_score(df['Y'], y_pred))  # Посчитали коэффициент детерминации r2
#
# x2 = pd.DataFrame(df['X2'])  # Показываем что наш объект DataFrame, и после трансформации передаем как переменную в регрессию fit
# # reg = LinearRegression()
# # reg.fit(x, df['Y'])
# # print(reg.coef_, reg.intercept_)
# # y_pred = reg.predict(x)
# # print(r2_score(df['Y'], y_pred))  # Посчитали коэффициент детерминации r2
#
# y_pred1 = lin_reg(x1, df['Y'])
# y_pred2 = lin_reg(x2, df['Y'])
#
# # lin_reg(x1, df['Y'])
# # lin_reg(x2, df['Y'])
#
# plt.plot(df['X1'], df['Y'], 'o')
# plt.plot(df['X1'], y_pred1)
# plt.show()
#
# plt.plot(df['X2'], df['Y'], 'o')
# plt.plot(df['X2'], y_pred2)
# plt.show()


###################################################################################
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.model_selection import train_test_split  # Делит нашу выборку на тестовую и обучающую
# from sklearn.metrics import mean_absolute_percentage_error  # MAPE
#
#
# def lin_reg(x, y, name):
#     x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)
#     regr = LinearRegression()
#     regr.fit(x_train, y_train)
#     y_pred = regr.predict(x_train)
#     y_pred2 = regr.predict(x_test)
#     print(regr.coef_)  # m
#     print(regr.intercept_)  # b
#     print(r2_score(y_train, y_pred))
#     print(mean_absolute_percentage_error(y_test, y_pred2))
#     print('============')
#
#     plt.plot(x_train[name], y_train, 'o')
#     plt.plot(x_train[name], y_pred)
#     plt.show()
#
#     return y_pred, y_pred2
#
#
# df = pd.read_csv('Dannye.csv', delimiter=';', encoding='cp1251')
# print(df.info())
#
# sns.heatmap(df.corr(), annot=True, cbar=False)
# plt.show()
#
# x1 = pd.DataFrame(df['X1'])
# x2 = pd.DataFrame(df['X2'])
#
# y_pred1 = lin_reg(x1, df['Y'], 'X1')
# y_pred2 = lin_reg(x2, df['Y'], 'X2')


###################################################################################
# Множественная регрессия

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split  # Делит нашу выборку на тестовую и обучающую
from sklearn.metrics import mean_absolute_percentage_error  # MAPE


def lin_reg(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)
    regr = LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_train)
    y_pred2 = regr.predict(x_test)
    print(regr.coef_)  # m
    print(regr.intercept_)  # b
    print(r2_score(y_train, y_pred))
    print(mean_absolute_percentage_error(y_test, y_pred2))
    print('============')

    # plt.plot(x_train[name], y_train, 'o')
    # plt.plot(x_train[name], y_pred)
    # plt.show()

    return y_pred, y_pred2


df = pd.read_csv('Dannye.csv', delimiter=';', encoding='cp1251')
print(df.info())

sns.heatmap(df.corr(), annot=True, cbar=False)
plt.show()

x1 = df[['X1', 'X2']]

y_pred1 = lin_reg(x1, df['Y'])


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

###################################################################################
#
