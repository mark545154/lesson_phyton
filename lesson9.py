###################################################################
# Задача 1. Маркетологу дано задание вычислить результативность рекламной кампании интернет магазина по Москве и Санкт-Петербургу

def count_arpu(revenue, people):
    return revenue / people


# arpu_moscow = round(count_arpu(63000, 4900), 2)
# arpu_spb = round(count_arpu(48000, 3500), 2)
# print(arpu_moscow, arpu_spb)

# string_in = input('Введите строку для вывода: ')

def visual(people_one, revenue, string=input('Введите строку для вывода: ')):
    number = round(count_arpu(revenue, people_one), 2)

    print(string + str(number))


visual(people_one=4900, revenue=63000, string='Доход от одного пользователя по Мск составил ')  # именованный
visual(people_one=3500, revenue=48000, string='Доход от одного пользователя по Спб составил ')  # именованный

visual(4900, 63000)  # позиционный
visual(3500, 48000)  # позиционный

visual(4900, 63000, 'Доход от одного пользователя по Мск составил ')
visual(3500, 48000, 'Доход от одного пользователя по Спб составил ')


# visual(round(count_arpu(63000, 4900), 2))
# visual(round(count_arpu(48000, 3500), 2))

# visual(string_in,round(count_arpu(63000, 4900), 2))
# visual(input('Введите строку для вывода: '), round(count_arpu(48000, 3500), 2))


# visual('Доход от одного пользователя по Мск составил ',
#        round(count_arpu(63000, 4900), 2))

# visual('Доход от одного пользователя по Спб составил ',
#        round(count_arpu(48000, 3500), 2))


###################################################################
#

def printing_string(string):
    if len(string) >= 3:
        print(string[2])

    if len(string) >= 2:
        print(string[-2])
        print(string[:-2])

    if len(string) >= 5:
        print(string[:5])

    print(string[::2])
    print(string[1::2])
    print(string[::-1])
    print(string[::-2])

    print(len(string))


printing_string('Привет')


###################################################################
# Задача 2. Создадим функцию, классифицирующую источник трафика на платный и бесплатный. Даны источники трафика

def traffic_source(source=input('Источник трафика: ')):
    if source == 'Инфопартнер' or source == 'Прямой заход':
        return 'Это бесплатный переход'
    elif source == 'Яндекс' or source == 'Инстаграм':
        return 'Это платный переход'


print(traffic_source())


###################################################################
# Практическая работа_Функции_доп дорешать задачи с 3
# Задача 3. Написать функцию сортировки вводимых из консоли 3х чисел по возрастанию и по убыванию.

def sort(num1, num2, num3):
    if num1 > num2 and num2 > num3:
        return 'Числа по убыванию ' + str(num1), str(num2), str(num3)
    elif num1 < num2 and num2 < num3:
        return 'Числа по возрастанию ' + str(num1), str(num2), str(num3)
    elif num2 > num1 and num1 > num3:
        return 'Числа по убыванию ' + str(num2), str(num1), str(num3)
    elif num2 < num1 and num1 < num3:
        return 'Числа по возрастанию ' + str(num2), str(num1), str(num3)
    elif num3 > num1 and num3 > num1:
        return 'Числа по убыванию ' + str(num3), str(num2), str(num1)
    elif num3 < num1 and num3 < num1:
        return 'Числа по возрастанию ' + str(num3), str(num2), str(num1)


print(sort(int(input('Введите первое число: ')),
           int(input('Введите второе число: ')),
           int(input('Введите третье число: '))))

###################################################################
# Задача 4. Написать функцию, реализующую игру в кости. Использовать функцию генерирования случайного значения

import random


def generating():
    cube1 = random.randint(1, 6)
    print('Значение первого кубика: ', cube1)  # Проверяем что выводит первый кубик
    cube2 = random.randint(1, 6)
    print('Значение второго кубика: ', cube2)  # Проверяем что выводит второй кубик
    result = cube1 + cube2  # Складываем значение двух кубиков
    return result


print(generating())


###################################################################
# Задача 5. С данной задачей вы уже знакомы.
# Вернитесь к заданию по расчету затрат на электроэнергию в зависимости от типа плиты

def electric(t1, t2, t3):
    result_electro = (t1 * 6.18) + (t3 * 5.15) + (t2 * 1.74)
    return 'Сумма оплаты за электроэнергию с электрической плитой составила: ', (round(result_electro), 2), ' руб.'


def gas(t1, t2, t3):
    result_gas = (t1 * 6.18) + (t3 * 5.92) + (t2 * 7.10)
    return 'Сумма оплаты за электроэнергию с газовой плитой составила: ', (round(result_gas), 2), ' руб.'


t1 = float(input('Введите показания по Тарифу 1 = '))
t2 = float(input('Введите показания по Тарифу 2 = '))
t3 = float(input('Введите показания по Тарифу 3 = '))
stove = input('Какая у Вас плита газ / электро?: ')

if stove == 'газ':
    result = gas(t1, t2, t3)
elif stove == 'электро':
    result = electric(t1, t2, t3)

print(result)


###################################################################
# Задача 6. Оформить задачу решения квадратного уравнения с использованием функций.
# Предусмотреть возможность вызова функции с 1 параметром для случаев неполного
# квадратного уравнения (вспоминаем аргументы со значением по умолчанию)

import math


# Функция square(), которая получает ссылку на некоторую функцию.
def square(func, a, b, c):
    d = func(a, b, c)  # Вызываем функцию с тремя параметрами
    if d < 0:
        # Если уравнение не имеет корней, функция возвращает пустой список.
        return []  # Уравнение не имеет решения
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)  # Нахождение корня x1
        x2 = (-b + math.sqrt(d)) / (2 * a)  # Нахождение корня x2
        return [x1, x2]  # Функция возвращает решение квадратного уравнения в виде списка.


# Функция, которая вычисляет дискриминант
def diskr(a, b, c):  # Функция принимает три параметра
    return b * b - 4 * a * c  # Формулой высчитываем дискриминант


# Передача функции diskr() как параметра в функцию square()
roots = square(diskr, 2,
               int(input('Введите значение b: ')),
               int(input('Введите значение c: ')))
if roots:
    print("x1 = ", roots[0])  # Выводим значение x1
    print("x2 = ", roots[1])  # Выводим значение x2
else:
    print("Уравнение не имеет корней")
