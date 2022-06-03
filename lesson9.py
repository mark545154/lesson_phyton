###################################################################
# Задача 1. Маркетологу дано задание вычислить результативность рекламной кампании интернет магазина по Москве и Санкт-Петербургу

# def count_arpu(revenue, people):
#     return revenue / people
#
#
# # arpu_moscow = round(count_arpu(63000, 4900), 2)
# # arpu_spb = round(count_arpu(48000, 3500), 2)
# # print(arpu_moscow, arpu_spb)
#
# # string_in = input('Введите строку для вывода: ')
#
# def visual(people_one, revenue, string=input('Введите строку для вывода: ')):
#     number = round(count_arpu(revenue, people_one), 2)
#
#     print(string + str(number))
#
#
# visual(people_one=4900, revenue=63000, string = 'Доход от одного пользователя по Мск составил ')  # именованный
# visual(people_one=3500, revenue=48000, string = 'Доход от одного пользователя по Спб составил ')  # именованный
#
# visual(4900, 63000)  # позиционный
# visual(3500, 48000)  # позиционный
#
# visual(4900, 63000, 'Доход от одного пользователя по Мск составил ')
# visual(3500, 48000, 'Доход от одного пользователя по Спб составил ')
#
# # visual(round(count_arpu(63000, 4900), 2))
# # visual(round(count_arpu(48000, 3500), 2))
#
# # visual(string_in,round(count_arpu(63000, 4900), 2))
# # visual(input('Введите строку для вывода: '), round(count_arpu(48000, 3500), 2))
#
#
# # visual('Доход от одного пользователя по Мск составил ',
# #        round(count_arpu(63000, 4900), 2))
#
# # visual('Доход от одного пользователя по Спб составил ',
# #        round(count_arpu(48000, 3500), 2))


###################################################################
#

# def printing_string(string):
#     if len(string) >= 3:
#         print(string[2])
#
#     if len(string) >= 2:
#         print(string[-2])
#         print(string[:-2])
#
#     if len(string) >= 5:
#         print(string[:5])
#
#     print(string[::2])
#     print(string[1::2])
#     print(string[::-1])
#     print(string[::-2])
#
#     print(len(string))
#
#
# printing_string('Привет')


###################################################################
# Задача 2. Создадим функцию, классифицирующую источник траффика на платный и бесплатный. Даны источники траффика
def traffic_source(source=input('Источник трафика: ')):
    if source == 'Инфопартнер' or source == 'Прямой заход':
        return 'Это бесплатный переход'
    elif source == 'Яндекс' or source == 'Инстаграм':
        return 'Это платный переход'


print(traffic_source())

###################################################################
# Практическая работа_Функции_доп дорешать задачи с 3
