###################################################################################
#
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Пациенты_new.csv', delimiter=';', encoding='cp1251')

print(df)
print(df.info())
print(df.duplicated().sum())
df = df.drop_duplicates()
# print(df.duplicated(subset='card_num').value_counts())
df.dropna(subset=['gender', 'birth'], inplace=True)
print(df.info())

print(df.gender.unique())

df['birth'] = pd.to_datetime(df.birth, dayfirst=True)
df['last_visit'] = pd.to_datetime(df.last_visit, dayfirst=True)

df['age'] = (pd.Timestamp('now') - df.birth).astype('m8[Y]')
df = df[df.age < 100]
df = df[df.sales_cost < 1000000]

print(df.head())

plt.hist(df.age, bins=10)
plt.show()
plt.hist(df.gender, bins=50)
plt.show()

df_young = df[df.age < 18]
df_adult = df[df.age >= 18]

plt.scatter(df_young.age, df_young.sales_cost)
plt.show()
plt.scatter(df_adult.age, df_adult.sales_cost)
plt.show()

plt.hist(df_young.age, bins=10)
plt.show()
plt.hist(df_adult.age, bins=10)
plt.show()

print(df.age.mean())
print(df.age.std())

print(df_adult.age.median())
print(df_adult.age.mean())
print(df_adult.age.std())

print(df_young.age.median())
print(df_young.age.mean())
print(df_young.age.std())

df_new = df[(df.visits_num <= 2) & (df.last_visit > pd.to_datetime('01.05.2022', dayfirst=True))]

print(df_new)

df_adult['aver'] = df_adult.sales_cost / df_adult.visits_num

print(df_adult.aver.mean())
