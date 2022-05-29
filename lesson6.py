########################################################################!!!
def greet_customer(grocery_store, special_item):
    print("Добро пожаловать в магазин "+ grocery_store + ".")
    print("Специальное предложение для вас - " + special_item + ".")
    print("Удачных покупок!")

greet_customer("Stu's Staples", "папайя")

########################################################################!!!
# Ключевые аргументы
name = '"Загрузки"'

def create_spreadshhet(title, row_count=1000):

    string = 'Создание электронной таблицы с именем ' + str(title) + ' с ' + str(row_count) + ' строк'
    print(string)

create_spreadshhet(name, 10)
create_spreadshhet("'Меню'", 30)

########################################################################!!!
# Возвращаемые значения
name = '"Загрузки"'

def create_spreadshhet(title, row_count=1000):

    string = 'Создание электронной таблицы с именем ' + str(title) + ' с ' + str(row_count) + ' строк'
    return (string)

s = create_spreadshhet(name, 10)
print(s + '!')

########################################################################!!!
# Задание. Функция define_age в script.pyc создает переменную с именем age, которая представляет собой разницу между текущим годом и годом рождения

def calc_age (current_year, birth_year):
    age = current_year - birth_year
    return age

dads_age = calc_age(2049, 1953)
my_age = calc_age(2049, 1993)

print('Мне ' + str(my_age) + ' лет, ' + 'моему отцу ' + str(dads_age) + ' лет.')

########################################################################!!!
# Несколько возвращаемых значений
def square_point(x_value, y_value):
 x_2 = x_value * x_value
 y_2 = y_value * y_value
 return x_2, y_2

x_square, y_square = square_point(1, 3)
print(x_square)
print(y_square)

########################################################################!!!
# Задание. Напишите функцию с именем get_boundaries (), которая принимает два параметра

def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target

    return low_limit, high_limit

l_limit, h_limit = get_boundaries(100, 20)
print('Нижний предел: ' + str(l_limit) + ', верхний предел: ' + str(h_limit))

########################################################################!!!
# Области видимости

header_string = "Специальное предложение для вас - "

def create_special_string(special_item):
    return header_string + special_item + "."

print("Я не люблю " + create_special_string('бананы'))

########################################################################!!!
# Задание.Вне функции calc_age () попробуйте вывести current_year.
current_year = 2048

def calc_age(birth_year):
    age = current_year - birth_year
    return age

print(calc_age(1982))
print(current_year)

########################################################################!!!
# Задание. Определите функцию с именем repeat_stuff

def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats

result = repeat_stuff('Row ', 3)
lyrics = result + ' Your Boat'
song = repeat_stuff('Row ')

print(song)

########################################################################!!!
# Задача. Необходимо создать метод, который проверяет, дает ли результат возведение в степень ответ, превышающий 5000

def exp_num(number, exp):
    result = number**exp # Возводим в степень

    if result>=5000:
        return True
    else:
        return False

print(exp_num(int(input('Введите основание: ')), int(input('Введите степень: '))))

print(exp_num(2, 3))

########################################################################!!!
# Задача 2. Давайте создадим приложение для проверки, попадает ли число в определенный диапазон.

test = int(input('Введите число: '))
def test_number(number, lower_limit, higher_limit):

    if lower_limit<=number<=higher_limit:
        return True
    else:
        return False
print(test_number(test, int(input('Введите нижнюю границу: ')), int(input('Введите верхнюю границу: '))))

########################################################################!!!
# Задача 3. Нам нужно написать программу, которая проверяет разные имена и определяет, равны ли они.

def comparison (name1, name2):

    if name1 == name2:
        return True
    else:
        return False

res = comparison(input('Введите имя 1: '), input('Введите имя 2: '))
print(res)

print(comparison('Mary', 'Mary')) # True
print(comparison('Mary', 'mary')) # False

########################################################################!!!
# Задача 4. Есть некоторые ситуации, которых обычно следует избегать при программировании с использованием условных операторов.

def num(num1, num2):
    if num1>num2 and num1<num2:
        return True
    else:
        return False
print(num(input('Введите значение 1: '), input('Введите значение 2: '))) # Всегда будет False

########################################################################!!!
# Задача 5. Мы хотим создать функцию, которая поможет нам оценивать фильмы.

def reiting_film(reiting):

    if reiting<=5:
        return 'Избегай любой ценой'
    elif reiting<9:
        return 'Это было весело'
    else:
        return 'Отлично!'

print(reiting_film(int(input('Введите рейтинг фильма: '))))

########################################################################!!!
# Задача 6. Необходимо выбрать, какое число из трех входных значений является наибольшим, используя условные операторы.

def result(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return 'Число 1 больше чем два других числа ', num1
    elif num2 > num1 and num2 > num3:
        return 'Число 2 больше чем два других числа ', num2
    elif num3 > num1 and num3 > num2:
        return 'Число 3 больше чем два других числа', num3
    else:
        return 'Ничья!'

print (result (int(input('Число 1: ')),int(input('Число 2: ')), int(input('Число 3: '))))

########################################################################!!!
# Задача 7. Давайте создадим несколько функций, которые помогут нам решать математические задачи!

num1 = 10 # Степень возведения числа

def enth_power(num2):
    summa = num2**num1
    return summa
print(enth_power(int(input('Введите число, для возведения в десятую степень: '))))


########################################################################!!!
# Еще одна полезная функция для решения математических задач - функция извлечения квадратного корня

def square_root(num):
    sqrt = num**(0.5)
    return 'Квадратный корень из числа ' + str(num) + ' это ' + str(sqrt)
print(square_root(int(input('Вариант 1! Введите число для извлечения квадратного корня: '))))


########################################################################!!!
# ещё один вариант математических задач - функция извлечения квадратного корня

import math
def square_root(num):
    sqrt = math.sqrt(num)
    return 'Квадратный корень из числа ' + str(num) + ' это ' + str(sqrt)
print(square_root(int(input('Вариант 2! Введите число для извлечения квадратного корня: ')))) # Если ввести к примеру -25 (получим ValueError: math domain error)


########################################################################!!!
# Задача 8. Далее мы создадим функцию, которая вычисляет процент выигранных игр.

# win - выигравших
# los - проигравших
# gen - общее количество игр, используя количество побед и поражений.

def win_games(win, los): # Определите заголовок функции с двумя параметрами, выигрышами и проигрышами.
    gen = win + los # общее количество игр
    kof_win = win / gen * 100  # Получите коэффициент выигрышей

    return ' Общее количество игр: ' + str(gen) + ' Коэффициент выигрыша: ' + str(kof_win) + '%'
res = win_games(int(input('Введите кол-во выигравших игр: ')), int(input('Введите кол-во проигравших игр: ')))
print(res)


########################################################################!!!
# Задача 9. Давайте создадим функцию, которая принимает среднее значение двух чисел

def sum_gen(num1, num2):
    sum = num1 + num2 #  Рассчитайте сумму двух чисел
    res = sum / 2
    return 'Среднее значение двух чисел будет: ' + str(res)
print(sum_gen(int(input('Введите первое число: ')), int(input('Введите второе число: '))))


########################################################################!!!
# Задача 10. В данной задаче необходимо вычислить остаток от деления

def sum_gen(num1, num2):
    res1 = num1 * 2
    res2 = num2 / 2
    final = res1 / res2
    return 'Остаток от деления двух чисел будет: ' + str(final)
print(sum_gen(int(input('Введите 1 число: ')), int(input('Введите 2 число: '))))


########################################################################!!!
# Задача 11. Создадим функцию, которая выводит в консоль и возвращает значения

def res_sum(num):
    sum1 = num * 2
    sum2 = num * 3
    final = sum2 * 3
    return ('''
    Входное число: %s
    Число в 2 раза больше исходного: %s
    Число в 3 раза больше исходного: %s
    В 3 раза больше исходного числа: %s
    ''' % (num, sum1, sum2, final))
print(res_sum(int(input('Введите число: '))))


########################################################################!!!
# Задача 11. Допустим, мы идем в ресторан и решаем оставить чаевые

def tip_calculation(total, tips = 0.03): # 3% оставим на чай
    final_sum = total * tips
    return 'Сумма чаевых составит: ' + str(final_sum) + ' руб.'
print(tip_calculation(int(input('Введите сумму заказа: '))))






















