########################################################################
#
my_fruit = "blueberry"
counter = 0
for letter in my_fruit:
    if letter == 'b':
        counter += 1  # counter = counter + 1

print(counter)  # Считает кол-во 'b' в слове и выводит 2, т.к. есть две 'b' в слове

########################################################################
# Напишите функцию с именем letter_check, которая принимает два ввода: слово и букву.

name_chek = 'bla bla bla \'a'


def letter_check(word, letter):
    for bukva in word:
        if bukva == letter:
            return True
    return False


print(letter_check(name_chek, 'a'))


########################################################################

def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False


print(letter_check('door', 'd'))


########################################################################

def letter_check(word, letter):
    return letter in word


print(letter_check('blueberry', 'blue'))  # True


########################################################################
# Задание1. Напишите функцию с именем contains, которая принимает два аргумента

def contains(big_string, little_string):
    return little_string in big_string


print(contains("watermelon", "melon"))  # True
print(contains("watermelon", "berry"))  # False


########################################################################
# Напишите функцию с именем common_letters, которая принимает два аргумента. должен вернуть ['a'].

def common_letters(string_one, string_two):
    s = ''
    for letter1 in string_one:  # Берёт букву из строки 1
        for letter2 in string_two:  # Сравнивает с каждой буквой строки
            if letter1 == letter2:  # Если совпали
                if letter1 not in s:  # Проверяет нет ли ее уже в строке
                    s += letter1  # Если нет, то запишет
    return s


print(common_letters("banana", "cream"))


########################################################################
# Упрощённый вариант. Напишите функцию с именем common_letters, которая принимает два аргумента. должен вернуть ['a'].

def common_letters(string_one, string_two):
    s = ''
    for letter1 in string_one:  # Берёт букву из строки 1
        if letter1 in string_two:  # Проверяет ее наличие в строке 2
            if letter1 not in s:  # Если ее нет еще нет в s
                s += letter1  # Если нет, то запишет
    if s == '':
        return 'Букв нет'
    else:
        return s


print(common_letters("banana", "cream"))


#########################################################################
# Задание1. Island’s Limited Company снова заручилась вашей помощью, чтобы создать функцию для создания имени пользователя и пароля.

def username_generator(first_name, last_name):
    if len(first_name) <= 3:
        username_part = first_name
    else:
        username_part = first_name[:3]

    if len(last_name) <= 4:
        username_part2 = last_name
    else:
        username_part2 = last_name[:4]
    return username_part + username_part2


login = username_generator('Abe', 'Simpson')


# Теперь что касается временного пароля

def password_generator(name):
    password = name[-1] + name[:-1]
    return password


print(login)
print(password_generator(login))


# print(password_generator('AbeSimp'))

######################################################################### Прокоментировать код!
# Комментирование кода!
def username_generator(first_name, last_name):  # Создаём функцию которая принимает два параметра
    if len(first_name) <= 3:  # Проверяет длину параметра first_name, если меньше или равен 3
        username_part1 = first_name  # записывает в переменную
    else:  # иначе
        username_part1 = first_name[0: 3]  # записывает в переменную с нулевого по третий символ

    if len(last_name) <= 4:  # Проверяет длину параметра last_name, если меньше или равен 4
        username_part2 = last_name  # записывает в переменную
    else:  # иначе
        username_part2 = last_name[0: 4]  # записывает в переменную с нулевого по четвёртый символ

    return username_part1 + username_part2  # возвращает переменные которые были записаны и соединяет их


login = username_generator('Abe', 'Simpson')  # Задаём два параметра функции, которые будут обработаны функцией


# https://pythontutor.com/render.html#mode=display
def password_generator(name):  # Создаём функцию которая принимает один параметр
    password = ""  # Определяем переменную с пустым значением
    x = -1  # Определяем переменную со значением -1
    for step in name:  # Создаём цикл шага с проверкой параметра
        password += name[x]  # Проверяем пустой password и если он пустой увеличиваем ему значение на 1
        x += 1  # Проверяем переменную x и прибавляем в нему 1 в каждом цикле
    return password  # Возвращаем значение


# def password_generator2 (name):
#   password=name[-1]+name[:-1]
#   return password

# username_generator (first_name,last_name)

print(login)  # Выводим значение переменной, которое получили в первой функции
print(password_generator(login))  # Выводим значение второй функции, которое прогоняли через цикл


#########################################################################

def password_generator(first_name, last_name):
    return first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]


print(password_generator('Джордж', 'Вашингтон'))  # рджтон


# Задание. Используйте отрицательные индексы, чтобы найти предпоследний символ в slogan
def second_to_last(slogan):
    return slogan[len(slogan) - 2]


print(second_to_last('Мечты сбываются'))  # с


# Задание. Используйте отрицательные индексы, чтобы создать фрагмент из последних 4 символов в slogan
def second_to_last(slogan):
    final_word = slogan[len(slogan) - 4:]
    return final_word


print(second_to_last('Мечты сбываются'))  # ются


###################################################################
def last_sumb(slogan):
    return slogan[-2], slogan[-4:]


result = last_sumb('Мечты сбываются')  # ('с', 'ются')
print(result)


# Задание. К сожалению, отдел кадров, похоже, допустил небольшую опечатку и прислал неправильное имя first_name
def first_latter(first_l, first_name):
    return first_l + first_name[1:]


print(first_latter('К', 'Дрис'))  # Крис
print(first_latter('Л', 'Нюси'))  # Люси


###################################################################

# Дана строка.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.
def string_letter(letter1):
    if len(letter1) < 5:
        return 'Введите текст больше 5-ти символов'
    return letter1[2], \
           letter1[-2], \
           letter1[:5], \
           letter1[:-2], \
           letter1[0::2], \
           letter1[1::2], \
           letter1[::-1], \
           letter1[::-2], \
           len(letter1)


print(string_letter('Привет!'))
