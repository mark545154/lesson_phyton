import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# %matplotlib inline
from sklearn import tree
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('vkr_winequality-red.csv', delimiter=',')
# print(df)
print(df.info())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.shape)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.head())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.duplicated().sum()) # 240
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.isnull())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.isnull().sum())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.describe())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
# print(df.head(6))
# print(df.iloc()[0])
# print(df.columns)
# print(df.tail())

# print(df['alcohol'].mean())
# print(df['alcohol'].unique())

# Здесь мы видим, что фиксированная кислотность не дает никаких указаний для классификации качества
fig = plt.figure()
sns.barplot(x='quality', y='fixed acidity', data=df, palette='light:#5A9')
plt.xlabel('качество', fontsize=8, fontweight="bold")
plt.ylabel('фиксированная кислотность', fontsize=8, fontweight="bold")
# plt.show()
# plt.savefig('one_graf.png')

# Здесь мы видим, что это довольно слабая тенденция к снижению летучей кислотности по мере того, как мы повышаем качество
fig = plt.figure()
sns.barplot(x='quality', y='volatile acidity', data=df)
plt.xlabel('качество', fontsize=8, fontweight="bold")
plt.ylabel('летучая кислотность', fontsize=8, fontweight="bold")
# plt.show()
# plt.savefig('two_graf.png')

# Состав лимонной кислоты повышается по мере того, как мы повышаем качество вина
fig = plt.figure()
sns.barplot(x='quality', y='citric acid', data=df)
plt.xlabel('качество', fontsize=8, fontweight="bold")
plt.ylabel('лимонная кислота', fontsize=8, fontweight="bold")
# plt.show()
# plt.savefig('three_graf.png')

# Остаточный сахар влияет на качество не так заметно, как например лимонная кислота.
fig = plt.figure()
sns.barplot(x='quality', y='residual sugar', data=df)
plt.xlabel('качество', fontsize=8, fontweight="bold")
plt.ylabel('остаточный сахар', fontsize=8, fontweight="bold")
# plt.show()
# plt.savefig('four_graf.png')

# Смотрим по графику как влияет pH на качество
fig = plt.figure()
sns.barplot(x='quality', y='pH', data=df)
plt.xlabel('качество', fontsize=8, fontweight="bold")
plt.ylabel('pH', fontsize=8, fontweight="bold")
# plt.show()
# plt.savefig('five_graf.png')

# Смотрим как влияет плотность на качество
fig = plt.figure()
sns.barplot(x='quality', y='density', data=df)
plt.xlabel('качество', fontsize=8, fontweight="bold")
plt.ylabel('Плотность', fontsize=8, fontweight="bold")
# plt.show()
# plt.savefig('six_graf.png')

# Уровень алкоголя также повышается по мере повышения качества вина
fig = plt.figure()
sns.barplot(x='quality', y='alcohol', data=df)
plt.xlabel('качество', fontsize=8, fontweight="bold")
plt.ylabel('Алкоголь', fontsize=8, fontweight="bold")
# plt.show()
# plt.savefig('seven_graf.png')

# Перепроверить!!! [15]
# Выводим гистограмму с использованием графика
df['quality'].value_counts().plot.bar()
plt.xlabel('"Ось X"', fontsize=8, fontweight="bold")
plt.ylabel('"Ось Y"', fontsize=8, fontweight="bold")
# plt.show()

# Перепроверить!!! [16]
df['quality'] = df['quality'].map({
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 1,
    8: 1
})
sns.countplot(df['quality'])
# plt.show()

# Теперь разделяем данные на переменную ответа и переменную объектов
X = df.drop('quality', axis=1)
y = df['quality']

# Обучающее и тестовое разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
pred_dtc = dtc.predict(X_test)

# Теперь выводим и смотрим как работает наша модель
print(classification_report(y_test, pred_dtc))

# Точность 86%

