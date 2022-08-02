###################################################################################
# - - - - - - Машинное обучение с использованием Scikit-learn - - - - - - #

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn import preprocessing
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import MinMaxScaler
#
# df = pd.read_csv('bank-marketing.csv')
# print(df.info())
# print(df.isnull().sum())  # Проверяем пропуски
#
# print(df['response'].unique())  # Проверяем уникальность на бинарную классификацию [0 1]
# print(df['response'].value_counts())  # Смотрим кол-во бинарной классификации
# # print(df.duplicated().sum())  # Смотрим кол-во дубликатов
# print(df.duplicated(subset=(df.columns[:-2])).sum())  # Смотрим кол-во противоречий
#
# print(df['targeted'].value_counts())
#
# print(df.drop(['default', 'day', 'contact', 'month', 'poutcome', 'y', 'marital-education'], inplace=True,
#               axis=1))  # Удаляем не нужные колонки
# print(df.info())
#
# print(df.describe())
#
# # df = df[df['salary'] > 0]  # Указываем чтобы в колонке salary было минимальное значение выше 0
# # print(df)  # Смотрим остаток кол-ва строк и колонок
# print(df.describe())  # Выводим значения, чтобы посмотреть min. До max. Значения
#
# # df1 = df[df['salary'] == 0]  # Проверяем на 0
# # print(df1)
#
# sns.barplot(data=df, x='age group', y='response')  # Строим гистограмму
# plt.show()

###################################################################################
#

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('diabetes.csv')
# print(df)
# print(df.isnull().sum())
# print(df.Outcome.value_counts())
# print(df.duplicated().sum())
# print(df.describe())
#
# sns.histplot(data=df, x=df['Age'])
# plt.show()
#
# # df1 = df[df.Age > 60]
# # print(df1)
#
# df1 = df[df.BloodPressure < 40]
# df1 = df1[['Age', 'Outcome', 'BloodPressure']]
# print(df1)

###################################################################################
#
import pandas as pd

df = pd.read_csv('Training Data.csv')
print(df.info())

print(df.duplicated(subset=(df.columns[1:])).sum())
print(df.Risk_Flag.value_counts())

###################################################################################
#

###################################################################################
#
