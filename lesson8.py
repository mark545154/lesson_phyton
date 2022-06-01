########################################################################
#
# my_fruit = "blueberry"
# counter = 0
# for letter in my_fruit:
#     if letter == 'b':
#         counter += 1  # counter = counter + 1
#
# print(counter)  # Считает кол-во 'b' в слове и выводит 2, т.к. есть две 'b' в слове


########################################################################
# Напишите функцию с именем letter_check, которая принимает два ввода: слово и букву.

# name_chek = 'bla bla bla \'a'
#
#
# def letter_check(word, letter):
#     for bukva in word:
#         if bukva == letter:
#             return True
#     return False
#
#
# print(letter_check(name_chek, 'a'))

########################################################################

# def letter_check(word, letter):
#     if letter in word:
#         return True
#     else:
#         return False
#
#
# print(letter_check('door', 'd'))

########################################################################

# def letter_check(word, letter):
#     return letter in word
#
#
# print(letter_check('blueberry', 'blue'))  # True


########################################################################
# Задание1. Напишите функцию с именем contains, которая принимает два аргумента

# def contains(big_string, little_string):
#     return little_string in big_string
#
#
# print(contains("watermelon", "melon"))  # True
# print(contains("watermelon", "berry"))  # False

########################################################################
# Напишите функцию с именем common_letters, которая принимает два аргумента. должен вернуть ['a'].

# def common_letters(string_one, string_two):
#     s = ''
#     for letter1 in string_one: # Берёт букву из строки 1
#         for letter2 in string_two: # Сравнивает с каждой буквой строки
#             if letter1 == letter2: # Если совпали
#                 if letter1 not in s: # Проверяет нет ли ее уже в строке
#                     s += letter1 # Если нет, то запишет
#     return s
#
#
# print(common_letters("banana", "cream"))

########################################################################
# Упрощённый вариант. Напишите функцию с именем common_letters, которая принимает два аргумента. должен вернуть ['a'].

# def common_letters(string_one, string_two):
#     s = ''
#     for letter1 in string_one:  # Берёт букву из строки 1
#         if letter1 in string_two:  # Проверяет ее наличие в строке 2
#             if letter1 not in s:  # Если ее нет еще нет в s
#                 s += letter1  # Если нет, то запишет
#     if s == '':
#         return 'Букв нет'
#     else: return s
#
#
# print(common_letters("banana", "cream"))

#########################################################################
# Задание1. Island’s Limited Company снова заручилась вашей помощью, чтобы создать функцию для создания имени пользователя и пароля.

# def username_generator(first_name, last_name):
#     if len(first_name) <= 3:
#         username_part = first_name
#     else:
#         username_part = first_name[:3]
#
#     if len(last_name) <= 4:
#         username_part2 = last_name
#     else:
#         username_part2 = last_name[:4]
#     return username_part + username_part2
#
#
# login = username_generator('Abe', 'Simpson')
#
#
# # Теперь что касается временного пароля
#
# def password_generator(name):
#     password = name[-1] + name[:-1]
#     return password
#
#
# print(login)
# print(password_generator(login))
# # print(password_generator('AbeSimp'))

######################################################################### Прокоментировать код!
#
def username_generator(first_name, last_name):
    if (len(first_name) <= 3):
        username_part1 = first_name
    else:
        username_part1 = first_name[0: 3]

    if (len(last_name) <= 4):
        username_part2 = last_name
    else:
        username_part2 = last_name[0: 4]

    return username_part1 + username_part2


login = username_generator('Abe', 'Simpson')


def password_generator(name):
    password = ""
    x = -1
    for step in name:  # https://pythontutor.com/render.html#mode=display
        password += name[x]
        x += 1
    return password


# def password_generator2 (name):
#   password=name[-1]+name[:-1]
#   return password

# username_generator (first_name,last_name)

print(login)
print(password_generator(login))