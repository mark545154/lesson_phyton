###################################################################################
# - - - - Визуализация данных с использованием библиотек Matplotlib и Seaborn - - - #

# 1.	Имеются 3 файла с данными о ценах поддержанных автомобилей марок Audi, BMW и Mercedes. Данные содержат следующие опции:
# модель автомобиля.
# год регистрации
# цена в евро.
# Тип коробки передач.
# расстояние пробега.
# Тип моторного топлива.
# налог - дорожный налог.
# mpg расход топлива (миль на галлон).
# объем двигателя в литрах.
# 2.	 Необходимо загрузить все файлы и объединить их в один набор данных.
# 3.	Добавить столбец с маркой авто (BMW, Mercedes или Audi)
# 4.	Вывести информацию о наборе данных. Сколько в наборе данных объектов? Есть ли пропуски?
# 5.	Проверить наличие дубликатов в данных. Сколько дубликатов в файле?
# 6.	Очистить данные от дубликатов\
# 7.	Построить график зависимости цены автомобиля от пробега.
# 8.	Построить гистограмму по цене.
# 9.	Построить нормальное распределение по цене.
# 10.	Построить столбчатую диаграмму цен по маркам автомобиля.
# 11.	Компания решила повысить цены на авто. Цены на авто с бензиновым двигателем будут повышены на 5%, на авто с дизельным – на 7%. Создать новый столбец с указанием новой цены авто.
# 12.	Удалить столбец старых цен

import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

files = glob.glob('auto*.csv')

df_list = []
for filenames in files:
    data = pd.read_csv(filenames)
    df_list.append(data)
    if 'audi' in filenames:
        data['brand'] = 'Audi'
    elif 'bmw' in filenames:
        data['brand'] = 'BMW'
    else:
        data['brand'] = 'Mercedes'

df = pd.concat(df_list)  # concat Объединяет файлы
print(df.info())
print(df.head())

# print(df.duplicated().sum())  # Проверяем на дубликаты
df.drop_duplicates(inplace=True)  # Удаляем дубликаты
df.reset_index(drop=True, inplace=True)
# df = df.drop_duplicates()  # Работает так же, как и строкой выше. Но без указания inplace=True
print(df.duplicated().sum())  # Проверяем на дубликаты

# plt.scatter(df.mileage, df.price)
# plt.show()

sns.scatterplot(data=df, x='mileage', y='price',
                color='red',
                palette=sns.color_palette(palette='deep'))
# sns.scatterplot(data=df, x='mileage', y='tax',
#                 palette=sns.color_palette(palette='rocket'))
print(df.price.describe())  # Выводим выбросы, если есть
plt.show()

plt.hist(df.price, bins=20)  # Выводим гистограмму
plt.show()

norm_price = np.random.normal(df.price.mean(), df.price.std(), size=1000)
plt.hist(norm_price, bins=20)
plt.show()
print(df[df.price == df.price.max()])  # Выводим самый дорогой авто
print(df[df.price == df.price.min()])  # Выводим самый дешёвый авто
print(df[df.price == df.price.median()])  # Выводим медиану по авто

df_group = df.groupby(by=['brand']).price.mean()  # Считаем среднюю цену по маркам автомобилей
print(df_group)  # Выводим в консоль, средние цены по маркам авто
plt.bar(df_group.index, df_group)  # Выводит столбчатые диаграммы
plt.show()

# 10.	Построить столбчатую диаграмму цен по маркам автомобиля
sns.barplot(data=df, x='brand', y='price', estimator=np.mean,
            palette='light:#5A9')  # Выводим тоже что и выше только с помощью библиотеки seaborn, но так же используется numpy (Выводим групировку по категориям)
plt.show()

# 11.	Компания решила повысить цены на авто. Цены на авто с бензиновым двигателем будут повышены на 5%, на авто с дизельным – на 7%. Создать новый столбец с указанием новой цены авто.
print(df.fuelType.unique())

print(df[df.fuelType == 'Diesel'])
# Перебираем по строкам и индексам
# for index, row in df.iterrows():
#
#     if row['fuelType'] == 'Petrol':
#
#         df.loc()[index, 'new_price'] = df.loc()[index, 'price'] * 1.05
#
#     elif row['fuelType'] == 'Diesel':
#         df.loc()[index, 'new_price'] = df.loc()[index, 'price'] * 1.07
#
#     else:
#         df.loc()[index, 'new_price'] = df.loc()[index, 'price']
#
# print(df[df.fuelType == 'Diesel'])


# Через lambda функцию, аналогично выше через for
df['new_price'] = df.apply(lambda row: row['price'] * 1.07 if row['fuelType'] == 'Diesel' else row['price'], axis=1)
df['new_price'] = df.apply(lambda row: row['price'] * 1.05 if row['fuelType'] == 'Petrol' else row['new_price'], axis=1)
print(df[df.fuelType == 'Diesel'])


# 12.	Удалить столбец старых цен
df.drop('price', inplace=True, axis=1)
print(df)

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
