###################################################################################
# - - - Машинное обучение с использованием Scikit-learn - - - - #

# Задание
# 1 Создайте функцию с именем euclidean_distance (), которая принимает два списка в
# качестве параметров с именами pt1 и pt2.
# В функции создайте переменную с именем distance, установите ее равной 0 и верните
# расстояние.
# 2. После определения расстояния создайте цикл for для просмотра размеров каждой точки.
# К расстоянию прибавьте квадрат разницы между каждым измерением.
# Помните, что в Python вы можете возвести переменную num в квадрат, используя num ** 2.
# 3. Вне цикла for извлеките квадратный корень из расстояния и верните это значение.
# 4. Выведите евклидово расстояние между [1, 2] и [4, 0].
# Выведите евклидово расстояние между [5, 4, 3] и [1, 7, 9].
# Почему вы не можете найти разницу между [2, 3, 4] и [1, 2]?

def euclidean_distance(pt1, pt2):
    distance = 0

    try:
        for index in range(len(pt1)):
            distance += (pt1[index] - pt2[index]) ** 2  # Расчитываем сумму квадратов разницы

        return distance ** 0.5  # Евклидово расстояние
    except IndexError:
        return 'Невозможно рассчитать расстояние!'


print(euclidean_distance([1, 2], [4, 0]))  # 3.605551275463989
print(euclidean_distance([5, 4, 3], [1, 7, 9]))  # 7.810249675906654
print(euclidean_distance([2, 4, 3], [1, 2]))  # Невозможно рассчитать расстояние!

###################################################################################
# Задание
# 1. Ниже euclidean_distance () создайте функцию с именем manhattan_distance (),
# которая принимает в качестве параметров два списка с именами pt1 и pt2.
# В функции создайте переменную с именем distance, установите ее равной 0 и верните ее.
# Аналогично предыдущей задачи с помощью цикла рассчитайте расстояние Манхэттена.
# Проверьте работу функции на тех же значениях, что и в предыдущей задаче.

def euclidean_distance(pt1, pt2):
    distance = 0

    try:
        for index in range(len(pt1)):
            distance += (pt1[index] - pt2[index]) ** 2  # Расчитываем сумму квадратов разницы

        return distance ** 0.5  # Евклидово расстояние
    except IndexError:
        return 'Невозможно рассчитать расстояние!'


def manhattan_distance(pt1, pt2):
    distance = 0

    try:
        for index in range(len(pt1)):
            distance += abs(pt1[index] - pt2[index])

        return distance  # Манхэттенское Расстояние
    except IndexError:
        return 'Невозможно рассчитать расстояние!'


print(euclidean_distance([1, 2], [4, 0]))  # 3.605551275463989
print(euclidean_distance([5, 4, 3], [1, 7, 9]))  # 7.810249675906654
print(euclidean_distance([2, 4, 3], [1, 2]))  # Невозможно рассчитать расстояние!

print(manhattan_distance([1, 2], [4, 0]))  # 5
print(manhattan_distance([5, 4, 3], [1, 7, 9]))  # 13
print(manhattan_distance([2, 4, 3], [1, 2]))  # Невозможно рассчитать расстояние!

###################################################################################
# Расстояние Хэмминга
# Расстояние Хэмминга - еще одна вариация формулы расстояния, которая немного
# отличается. Вместо того, чтобы находить разницу каждого измерения, расстояние
# Хэмминга заботится только о том, точно ли равны расстояния. При нахождении
# расстояния Хэмминга между двумя точками добавляется единица для каждого измерения,
# имеющего разные значения.

def hamming(pt1, pt2):
    distance = 0

    try:
        for index in range(len(pt1)):
            if pt1[index] != pt2[index]:
                distance += 1

        return distance  # Расстояние Хэмминга
    except IndexError:
        return 'Невозможно рассчитать расстояние!'


print(hamming([5, 4, 3], [1, 7, 9]))  # 3
print(hamming([5, 4, 3], [5, 4, 9]))  # 1

###################################################################################
# Градиентный спуск для сдвига
# Ищем для градиента b

import matplotlib.pyplot as plt


def get_gradient_at_b(x, y, b, m):
    N = len(x)  # Считаем кол-во x-ов
    diff = 0

    for i in range(N):
        diff += (y[i] - (m * x[i] + b))
    b_gradient = -2 / N * diff

    return b_gradient


# Ищем для градиента m
def get_gradient_at_m(x, y, b, m):
    N = len(x)
    diff = 0

    for i in range(N):
        diff += x[i] * (y[i] - (m * x[i] + b))
    m_gradient = -2 / N * diff

    return m_gradient


# Шаг градиента
def step_gradient(x, y, b_current, m_current, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)

    return b, m


def gradient_descent(x, y, learning_rate, num_iteration):
    b = 0
    m = 0

    for i in range(num_iteration):
        b, m = step_gradient(x, y, b, m, learning_rate)

    return b, m


month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Месяцы 12
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]  # Выручка за 12 месяцев

b, m = gradient_descent(month, revenue, 0.01, 1000)  # 0.01 - Это шаг
print(b, m)
y = [m * x + b for x in month]

plt.plot(month, revenue, 'o')
plt.plot(month, y)
plt.show()

###################################################################################
# С помощью библиотеки Scikit-learn

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]


def prepare_data(data, form):
    data = np.array(data)
    data = np.reshape(data, form)

    return data


def lin_reg(x, y):
    regr = LinearRegression()
    regr.fit(x, y)
    y_pred = regr.predict(x)
    # y_pred = [float(regr.coef_)*month[i]+float(regr.intercept_) for i in range(len(month))]  # Работает как и строкой выше
    print(regr.coef_)  # m
    print(regr.intercept_)  # b

    return (y_pred)


plt.plot(month, revenue, 'o')
plt.plot(month, lin_reg(prepare_data(month, (-1, 1)), prepare_data(revenue, (-1, 1))))
plt.show()

