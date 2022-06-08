#############################################################################
# - - - - - - - - - - - - Что такое список? - - - - - - - - #

# heights = [161, 170, 167, 164]
# names = ['Наталья', 'Алексей', 'Сергей', 'Марина']
# list1 = ['Наталья', 161]
# list2 = ['Алексей', 170]
# list3 = ['Сергей', 167]
# list4 = ['Марина', 164]

# names_heights = [['Наталья', 161], ['Алексей', 170], ['Сергей', 167], ['Марина', 164], ['Виктор', 168]]

# Создайте список списков, называемых возрастом, где каждый подсписок
# содержит имя учащегося и его возраст. Используйте следующие данные:
# • Андрей 15 лет
# • Дмитрий - 16 лет.

# ages = [['Андрей', 15], ['Дмитрий', 16]]

# names_heights = zip(names, heights)

# print(list(names_heights))

##############################################################
# Задание1. Используйте zip для создания новой переменной с именем 
# names_and_dogs_names, которая объединяет имена и имена собак в zip-объект.

# names = ['Ben', 'Holly', 'Ann']
# dogs_names = ['Sharik', 'Gab', 'Beethoven']

# names_and_dogs_names = zip(names, dogs_names)

# list_of_names_and_dogs_names = list(names_and_dogs_names)
# print(list_of_names_and_dogs_names)


# empty_list = []
# empty_list.append(5)
# print(empty_list)

# empty_list.append('hello')
# print(empty_list)

##############################################################
# Задание
# 1. Джихо работает в садовом магазине Petal Power. Он ведет учет заказов в списке, 
# который называется orders.
# Создайте список orders и используйте print, чтобы проверить заказы, которые он получил 
# сегодня.

# orders =['маргаритки', 'барвинок']
# print(orders)
# orders.append('тюльпаны')
# orders.append('розы')
# print(orders)

##############################################################
# 
# authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

# author_names = authors.split(', ')

# # print(author_names)

# author_last_names = []

# for author in author_names: #для каждого элемента author_names 

#     # author_last_names.append(author.split()[-1]) #разделяем имя и фамилию и берем фамилию (-1 элемент в новом списке). добавляем в список
#     author_last_names += [author.split()[-1]] 
# print(author_last_names)

##############################################################
# Задание
# 1. Джихо все еще обновляет свой список заказов. Он только что получил заказы на 
# «сирень» и «ирис»

# orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
# new_orders = orders + ['сирень', 'ирис']
# print(new_orders)


##############################################################
# 
# broken_prices = [5, 3, 4, 5, 4] + [4]
# print(broken_prices)

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_range = range(5, 12) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(my_range)) 

# my_list3 = range(1, 100, 10) # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
# print(list(my_list3)) 

# list4 = range(5, 15, 3) # [5, 8, 11, 14]
# print(list(list4))

# list5 = range(0, 40, 5) # [0, 5, 10, 15, 20, 25, 30, 35]
# print(list(list5))

##############################################################
# Задание
# 1. Измените list1 так, чтобы это был диапазон, содержащий числа, начинающиеся с 
# 0 и до 9, но не включая его.

# list1 = range(9)
# print(list(list1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

##############################################################
# Задания
# 1. Мария вводит данные клиентов для своего бизнеса в области веб-дизайна. Вы 
# поможете ей организовать свои данные

# first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
# age = []
# age.append('42')
# # print(age)
# all_ages = ['32', '41', '29']
# all_ages = all_ages + age
# # print(all_ages)
# name_and_age = zip(first_names, all_ages)
# # print(list(name_and_age)) 
# ids = range(0, 4)
# print(list(zip(ids, first_names, all_ages)))

##############################################################
# 
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list)) # 5


##############################################################
# Задание
# 1. Вычислите длину list1 и сохраните ее в переменной list1_len

# list1 = range (2, 20, 2)
# list1_len = len(list1)

# print(len(list1))

##############################################################
# 
# calls = ['Алексей', 'Владимир', 'Коснстантин', 'Дмитрий', 'Элеонора']
# index2 = calls[2]
# print(index2)


##############################################################
# Задание
# 1. Используйте квадратные скобки ([и]), чтобы выбрать элемент с индексом 4 из 
# списка сотрудников. Сохраните его в переменной index4.
# сотрудники = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
# index4 = сотрудники[4]
# print(index4) # Райан

# print(len(сотрудники)) # 7

##############################################################
# Задание
# 1. Используйте print и len, чтобы отобразить длину shopping_list.

# shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
# print(len(shopping_list))

# last_element = shopping_list[-1]
# print(last_element)

# element5 = shopping_list[5]
# print(element5)

##############################################################
# 
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# sublist = letters[1:6]
# print(sublist)

##############################################################
# Задание
# 1. Используйте print, чтобы проверить переменную beginning.
# suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
# beginning = suitcase [0: 2]
# Сколько элементов в списке?
# 2. Измените beginning, чтобы оно выделяло первые 4 элемента чемодана.
# 3. Создайте новый список под названием middle, содержащий два средних элемента 
# из чемодана.


# suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
# beginning = suitcase [0: 2]
# print(len(beginning))
# print(len(suitcase))

# beginning = suitcase[:4]
# print(beginning)

# middle = suitcase[2:4]
# print(middle)

##############################################################
# Срез списков II
# Если мы хотим выбрать первые 3 элемента списка, мы могли бы использовать 
# следующий код

# fruits = ['яблоко', 'банан', 'вишня', 'финик', 'банан', 'вишня']
# print(fruits[:3]) # ['яблоко', 'банан', 'вишня']
# print(fruits[:3:2]) # ['яблоко', 'вишня']
# print(fruits[::2]) # ['яблоко', 'вишня', 'банан']
# print(fruits[3:]) # ['финик', 'банан', 'вишня']
# print(fruits[-3:]) # ['финик', 'банан', 'вишня']
# print(fruits[-1::-1]) # ['вишня', 'банан', 'финик', 'вишня', 'банан', 'яблоко']
# print(fruits[1: :2]) # ['банан', 'финик', 'вишня']
# print(fruits[1:7:2]) # ['банан', 'финик', 'вишня']
# print(fruits[-3::2]) # ['финик', 'вишня']
# print(fruits[0::2]) # ['яблоко', 'вишня', 'банан']

##############################################################
# Подсчет элементов в списке
# Предположим, у нас есть список букв, который представляет буквы в слове 
# «Миссисипи»:

# letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
# num_i = letters.count('i')
# print(num_i)

##############################################################
# Задание
# Класс миссис Уилсон голосует за президента класса. Она сохранила голос каждого 
# студента в списке голосов.
# Используйте счетчик, чтобы определить, сколько студентов проголосовало за 
# «Джейка». Сохраните свой ответ как jake_votes.

# votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', \
#          'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', \
#          'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake','Jake', \
#          'Cassie', 'Laurie']

# jake_votes = votes.count('Jake')
# print(jake_votes) # 9

##############################################################
# Сортировка списков I
# Иногда нам нужно отсортировать список в числовом (1, 2, 3,…) или алфавитном (a, 
# b, c,…) порядке.
# Мы можем отсортировать список на месте, используя .sort (). Предположим, у нас 
# есть список имен:

# names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# print(names) # ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# names.sort() # sort() Сортирует по алфавиту

# names.sort(reverse=True) # Сортирует в обратном порядке. По убыванию!

# sorted_names = names.sort() # Вернёт None! Не присваивает переменной значение, т.к. не возвращает значение


# print(names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

##############################################################
# Задание
# Используйте сортировку для сортировки адресов

# addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
# addresses.sort() # изменяет сам список!!!

# print(addresses) # ['10 Downing St.', '12 Grimmauld Place', '1600 Pennsylvania Ave', '221 B Baker St.', '42 Wallaby Way', '742 Evergreen Terrace']

##############################################################
# Сортировка списков II
# Второй способ сортировки списка - использовать sorted. sorted отличается от .sort () 
# следующим

# names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

# sorted_names = sorted(names) # sorted() Это дает список, отсортированный по алфавиту

# print(names) # ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# print(sorted_names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

##############################################################
# Задание
# 1. Используйте сортировку, чтобы упорядочить игры и создать новый список с 
# именем games_sorted

# games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
# games_sorted = sorted(games)
# print(games_sorted) # ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']


##############################################################
# Задание
# 1. inventory - это список предметов, которые есть на складе для мебели Боба. Сколько 
# товаров на складе?
# Сохраните свой ответ в inventory_len
# 2. Выберите первый элемент в инвентаре. Сначала сохраните его в переменной first.
# 3. Выберите последний элемент из инвентаря и сохраните его в переменной last.
# 4. Выберите предметы из инвентаря, начиная с индекса 2 и до индекса 6, но не включая его.
# Сохраните свой ответ в inventory_2_6.
# 5. Выберите первые 3 предмета инвентаря и сохраните их в переменной first_3.
# 6. Сколько односпальных кроватей в инвентаре? Сохраните свой ответ в twin_beds.
# 7. Сортировка инвентаря с помощью .sort ()

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed',
             'king bed', 'dresser', 'dresser', 'table', 'table',
             'nightstand', 'nightstand', 'king bed', 'king bed',
             'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow',
             'pillow']
inventory_len = len(inventory)  # 19
print(inventory_len)

first = inventory[0]  # twin bed
print(first)

last = inventory[-1]  # pillow
print(last)

inventory_2_6 = range(2, 6)  # [2, 3, 4, 5]
print(list(inventory_2_6))

first_3 = inventory[:3]  # ['twin bed', 'twin bed', 'headboard']
print(first_3)

twin_beds = inventory.count('twin bed')  # 4
print(twin_beds)

inventory.sort()
print(inventory)
