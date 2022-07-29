import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split  # Делит нашу выборку на тестовую и обучающую
from sklearn.metrics import mean_absolute_percentage_error  # MAPE

df = pd.read_csv('housing.csv', delim_whitespace=True,
                 names=['CRIM', 'ZN', 'INDUS', 'CHAS',
                        'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B',
                        'LSTAT', 'MEDV'])
print(df.info())
sns.heatmap(df.corr().round(1), annot=True, cbar=False)
plt.show()
plt.scatter(df['CRIM'], df['MEDV'])
plt.show()

fig = plt.figure(figsize=(20, 20))
for index, item in enumerate(df.columns[:-1], start=1):

    s = fig.add_subplot(5, 3, index)
    s.set_title(item)  # Создаёт заголовок столбца
    plt.scatter(df[item], df['MEDV'])
plt.show()

plt.hist(df['MEDV'], bins=20)
plt.show()

print(df.describe())

def lin_reg(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, random_state=0)
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

    return y_pred

y = lin_reg(df[['LSTAT', 'RM']], df['MEDV'])



