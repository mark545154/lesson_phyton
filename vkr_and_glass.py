import pandas as pd
# Импортируем метод классификации ближайшего соседа
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('vkr_winequality-red.csv', delimiter=',')

print(df.info())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.shape)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.head())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.duplicated().sum())  # 240
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.isnull())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.isnull().sum())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print(df.describe())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

print(df['quality'].value_counts())
x_train, x_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]],
                                                    test_size=0.2, random_state=42)
sc = StandardScaler()

# Создание и конфигурирование модели ближайшего соседа (n_neighbors - количество соседей)
classif = KNeighborsClassifier(n_neighbors=8)
# Обучение модели методом ближайшего соседа (расчет расстояний) обучающая выборка
classif.fit(x_train, y_train)
# Проверка модели на тестовой выборке
y_pred = classif.predict(x_test)
# Результат расчета на тестовой выборке
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
# print(y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Вывод тестовой выборки для просмотра и сравнения с результатом расчета
(np.array(y_test)).reshape(1, -1)

# Расчет метрики точности классификации accuracy (отношение верно соотнесенных примеров с общим количеством объектов в тестовой выборке)
print(accuracy_score(y_test, y_pred))
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
pred_dtc = dtc.predict(X_test)

print(classification_report(y_test, pred_dtc))


