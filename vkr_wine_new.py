# Импортируйте Необходимые Библиотеки
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
import warnings
warnings.filterwarnings('ignore')
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)

# Импорт набора данных
df = pd.read_csv('vkr_winequality-red.csv', delimiter=',')
# print(df)


# Исследовательский Анализ Данных
df.sample()
print(df)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# проверка пропущенных значений
print(df.isnull().sum())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# проверка уникальности и типа для каждого столбца
df_nunique = pd.DataFrame([[col, df[col].nunique(), df[col].dtypes] for col in df.columns],
                          columns=['col', 'nunique', 'type'])
print(df_nunique)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Построение гистограммы
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='quality')
# plt.show()

# Построение гистограммы 2
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='fixed acidity', data=df)
# plt.show()

# Построение гистограммы 3
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='volatile acidity', data=df)
# plt.show()

# Построение гистограммы 4
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='citric acid', data=df)
# plt.show()

# Построение гистограммы 5
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='residual sugar', data=df)
# plt.show()

# Построение гистограммы 6
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='chlorides', data=df)
# plt.show()

# Построение гистограммы 7
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='free sulfur dioxide', data=df)
# plt.show()

# Построение гистограммы 8
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='total sulfur dioxide', data=df)
# plt.show()

# Построение гистограммы 9
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='density', data=df)
# plt.show()

# Построение гистограммы 10
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='pH', data=df)
# plt.show()

# Построение гистограммы 11
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='sulphates', data=df)
# plt.show()

# Построение гистограммы 12
plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='alcohol', data=df)
# plt.show()

# Преобразование в два класса
# df['quality'] = df['quality'].apply(lambda x: 'bad' if x < 6.5 else 'good')
df['quality'] = df['quality'].apply(lambda x: 'Плохое' if x < 6.5 else 'Хорошее')
print(df.quality.value_counts())
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

le = LabelEncoder()
df['quality'] = le.fit_transform(df['quality'])
X = df.drop('quality', axis=1)
y = df.quality
sc = StandardScaler()
X_scaled = sc.fit_transform(X)

# Моделирование
# Для части моделирования мы сравним 7 известных алгоритмов и приступим к оценке их средней точности с
# помощью k-кратной процедуры перекрестной проверки

# 1: Логистическая регрессия
#
# 2: KNN
#
# 3: SVC
#
# 4: Дерево решений
#
# 5: Случайный лес
#
# 6: Дополнительные деревья
#
# 7: Повышение градиента

# Применить Перекрестную проверку
# Определение классификаторов
kf = KFold(n_splits=3, shuffle=True, random_state=42)
Classifiers = []
Classifiers.append(LogisticRegression(random_state=42))
Classifiers.append(KNeighborsClassifier())
Classifiers.append(SVC(random_state=42))
Classifiers.append(DecisionTreeClassifier(random_state=42))
Classifiers.append(RandomForestClassifier(random_state=42))
Classifiers.append(ExtraTreesClassifier(random_state=42))
Classifiers.append(GradientBoostingClassifier(random_state=42))

# cross_val_score
cv_results = []
for Classifier in Classifiers:
    cv_results.append(cross_val_score(Classifier, X_scaled, y, cv=kf, scoring='accuracy', n_jobs=-1))

# cross_val_score Mean
cv_mean = []
for r in cv_results:
    cv_mean.append(np.mean(r))

# Создание фрейма данных из алгоритмов и параметра CrossValMeans
cv_res = pd.DataFrame({'algorithms': ['LogisticRegression',
                                      'KNN',
                                      'SVC',
                                      'DecisionTree',
                                      'RandomForest',
                                      'ExtraTrees',
                                      'GradientBoosting'], 'CV_mean': cv_mean}).sort_values(by='CV_mean',
                                                                                            ascending=False)
print(cv_res)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# train_test_split:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Масштабирование данных поезда
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

# Применить GridSearchCV
# определение параметров для GridSearchCV
param_grid_LR = {'penalty': ['l1', 'l2'],
                 'solver': ['lbfgs', 'newton_cg', 'liblinear'],
                 'C': np.logspace(-3, 3, 7), }

param_grid_KNN = {'n_neighbors': range(1, 31),
                  'weights': ['uniform', 'distance'],
                  'metric': ['euclidean', 'manhattan']}

param_grid_SVC = {'C': np.logspace(-3, 3, 7),
                  'gamma': [1, 0.1, 0.01, 0.001],
                  'kernel': ['rbf', 'poly', 'sigmoid']}

param_grid_DT = {'criterion': ['gini', 'entropy'],
                 'max_depth': np.arange(3, 15),
                 'max_features': ['sqrt', 'log2']}

param_grid_RF = {'n_estimators': [100, 200, 300, 400, 500],
                 'max_features': ['sqrt', 'log2'],
                 'max_depth': np.arange(3, 15),
                 'criterion': ['gini', 'entropy']}

param_grid_ET = {'n_estimators': [100, 200, 300, 400],
                 'max_features': ['sqrt', 'log2'],
                 'max_depth': np.arange(3, 15),
                 'criterion': ['gini', 'entropy']}

param_grid_GB = {'learning_rate': [0.01, 0.02, 0.03, 0.04],
                 'subsample': [0.9, 0.5, 0.2, 0.1],
                 'n_estimators': [100, 200, 300],
                 'max_depth': np.arange(5, 15)}

# GridSearchCV для логистической регрессии
grid_LR = GridSearchCV(Classifiers[0], param_grid_LR, cv=kf, n_jobs=-1)
grid_LR = grid_LR.fit(X_train_scaled, y_train)
print(grid_LR.best_params_)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# GridSearchCV для KNN
grid_KNN = GridSearchCV(Classifiers[1], param_grid_KNN, cv=kf, n_jobs=-1)
grid_KNN = grid_KNN.fit(X_train_scaled, y_train)
print(grid_KNN.best_params_)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# GridSearchCV для SVC
grid_SVC = GridSearchCV(Classifiers[2], param_grid_SVC, cv=kf, n_jobs=-1)
grid_SVC = grid_SVC.fit(X_train_scaled, y_train)
print(grid_SVC.best_params_)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# GridSearchCV для дерева решений
grid_DT = GridSearchCV(Classifiers[3], param_grid_DT, cv=kf, n_jobs=-1)
grid_DT = grid_DT.fit(X_train_scaled, y_train)
print(grid_DT.best_params_)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# GridSearchCV для случайного леса
grid_RF = GridSearchCV(Classifiers[4], param_grid_RF, cv=kf, n_jobs=-1)
grid_RF = grid_RF.fit(X_train_scaled, y_train)
print(grid_RF.best_params_)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# GridSearchCV для дополнительных деревьев
grid_ET = GridSearchCV(Classifiers[5], param_grid_ET, cv=kf, n_jobs=-1)
grid_ET = grid_ET.fit(X_train_scaled, y_train)
print(grid_ET.best_params_)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# GridSearchCV для повышения градиента
grid_GB = GridSearchCV(Classifiers[6], param_grid_GB, cv=kf, n_jobs=-1)
grid_GB = grid_GB.fit(X_train_scaled, y_train)
print(grid_GB.best_params_)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')


# Функция измерения
def measure(y_true, y_pred):
    accuracy = round(accuracy_score(y_true, y_pred), 4)
    recall = round(recall_score(y_true, y_pred), 4)
    precision = round(precision_score(y_true, y_pred), 4)
    f1 = round(f1_score(y_true, y_pred), 4)
    return pd.Series({'accuracy_score': accuracy,
                      'recall_score': recall,
                      'precision_score': precision,
                      'f1_score': f1})


# Создание модели LR
model_LR = LogisticRegression(C=0.001, penalty='l2', solver='liblinear', random_state=42)
model_LR = model_LR.fit(X_train_scaled, y_train)
y_pred = model_LR.predict(X_test_scaled)
acc_LR = measure(y_test, y_pred)
measure(y_test, y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Create KNN Model
model_KNN = KNeighborsClassifier(metric='manhattan', n_neighbors=24, weights='distance')
model_KNN = model_KNN.fit(X_train_scaled, y_train)
y_pred = model_KNN.predict(X_test_scaled)
acc_KNN = measure(y_test, y_pred)
measure(y_test, y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Создание модели SVC
model_SVC = SVC(C=10, gamma=1, kernel='rbf', random_state=42)
model_SVC = model_SVC.fit(X_train_scaled, y_train)
y_pred = model_SVC.predict(X_test_scaled)
acc_SVC = measure(y_test, y_pred)
measure(y_test, y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Созданная модель
model_DT = DecisionTreeClassifier(criterion='gini', max_depth=6, max_features='auto', random_state=42)
model_DT = model_DT.fit(X_train_scaled, y_train)
y_pred = model_DT.predict(X_test_scaled)
acc_DT = measure(y_test, y_pred)
measure(y_test, y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Создание радиочастотной модели
model_RF = RandomForestClassifier(criterion='gini', max_depth=11, max_features='auto', n_estimators=200,
                                  random_state=42)
model_RF = model_RF.fit(X_train_scaled, y_train)
y_pred = model_RF.predict(X_test_scaled)
acc_RF = measure(y_test, y_pred)
measure(y_test, y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Создание модели ET
model_ET = ExtraTreesClassifier(criterion='entropy', max_depth=14, max_features='auto', n_estimators=300,
                                random_state=42)
model_ET = model_ET.fit(X_train_scaled, y_train)
y_pred = model_ET.predict(X_test_scaled)
acc_ET = measure(y_test, y_pred)
measure(y_test, y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Создание модели ГБ
model_GB = GradientBoostingClassifier(learning_rate=0.04, max_depth=10, n_estimators=100, subsample=0.5,
                                      random_state=42)
model_GB = model_GB.fit(X_train_scaled, y_train)
y_pred = model_GB.predict(X_test_scaled)
acc_GB = measure(y_test, y_pred)
measure(y_test, y_pred)
print('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

final_result = pd.Series({'Logistic Regression': acc_LR['accuracy_score'],
                          'KNN': acc_KNN['accuracy_score'],
                          'SVC': acc_SVC['accuracy_score'],
                          'Decision Tree': acc_DT['accuracy_score'],
                          'Random Forest': acc_RF['accuracy_score'],
                          'Extra Trees': acc_ET['accuracy_score'],
                          'Gradient Boosting': acc_GB['accuracy_score']})

final_result = pd.DataFrame(final_result, columns=['Accuracy']).sort_values(by='Accuracy', ascending=False)

print(final_result)

# КАК мы можем видеть, Extra Trees обладает наилучшей производительностью по сравнению с другими алгоритмами.
