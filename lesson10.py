###################################################################
#

# stroka1 = 'HEllo'
# stroka2 = stroka1.lower()
#
# print(stroka2)  # hello
# print(stroka1.lower())  # hello
# print(stroka1.upper())  # HELLO
# print(stroka1.title())  # Hello

###################################################################
# Задание1. Вы программист, работающий в организации, которая пытается оцифровать и хранить стихи под названием «Poetry Passion».

# poem_title = "евгений онегин"
# poem_author = "Александр Сергеевич Пушкин"
#
# poem_title_fixed = poem_title.title()
# print(poem_title)  # евгений онегин
# print(poem_title_fixed)  # Евгений Онегин

###################################################################
#

# poem_title = "евгений онегин"
# poem_author = "Александр, Сергеевич, Пушкин"
#
# print(poem_author.split(', '))  # ['Александр', 'Сергеевич', 'Пушкин']

###################################################################
# Задание1. В переменной строка из первой строки стихотворения Ф.И. Тютчева «Весенние воды».

# line_one = "Еще в полях белеет снег"
# line_one_words = line_one.split()
# print(line_one_words) # ['Еще', 'в', 'полях', 'белеет', 'снег']

###################################################################
#
# name = "santana"
# print(name.split('n'))  # ['sa', 'ta', 'a']

###################################################################
# Задание. Ваш босс в прислал кучу имен авторов, которые он хочет, чтобы вы подготовили для импорта в базу данных

# authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kama la Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
#
# author_names = authors.split(', ')
# print(
#     author_names)  # ['Audre Lorde', 'William Carlos Williams', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kama la Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']
#
# # 3. Создайте еще один список с именем author_last_names, который содержит только фамилии поэтов в предоставленной
# # строке.
# author_last_names = []  # Объявляем переменную чтобы сделать список
# for author in author_names:  # Для каждого элемента author_names
#     author_last_names = author.split()[-1]  # разделяем имя и фамилию списка и берём только фамилию
#
#     print(author_last_names)  # Lorde
#     # Williams
#     # Mistral
#     # Toomer
#     # Qi
#     # Whitman
#     # Silverstein
#     # Boullosa
#     # Suraiyya
#     # Hughes
#     # Rich
#     # Giovanni

###################################################################
#
# smooth_chorus = \
# """And if you said, "This life ain't good enough."
# I would give my world to lift you up
# I could change my life to better suit your mood
# Because you're so smooth"""
#
# chorus_lines = smooth_chorus.split('\n')
# print(chorus_lines)
#
# new_chorus = ' '.join(chorus_lines)  # Метод join() объединяет! Противоположный split()
# print(new_chorus)

###################################################################
# Задание1. Организация прислала вам полный текст стихотворения Ф.И. Тютчева «Весенние воды». Они хотят, чтобы вы разбили стихотворение на отдельные строки.

# spring_waters_text = \
# """ Еще в полях белеет снег,
# А воды уж весной шумят —
# Бегут и будят сонный брег,
# Бегут, и блещут, и гласят…
# Они гласят во все концы:
# «Весна идет, весна идет,
# Мы молодой весны гонцы,
# Она нас выслала вперед!
# Весна идет, весна идет,
# И тихих, теплых майских дней
# Румяный, светлый хоровод
# Толпится весело за ней!..."""
#
# spring_waters_lines = spring_waters_text.split('\n')
# print(spring_waters_lines)

###################################################################
# .join()
import random


# my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
# print(' '.join(my_munequita))  # My Spanish Harlem Mona Lisa

###################################################################
# Задача 1. Компания просит вас разработать приложение, которое позволит генерировать имя пользователей в системе, как конкатенацию имени и инициалов. Необходимо создать переменные


# def genery(surname, name, patronymic):
#     login = surname + name[0] + patronymic[0]
#     return 'Имя пользователя ' + login + '@company.ru'
#
#
# print(genery('Имя', 'Фамилия', 'Отчество'))


# Далее пользователю необходимо задать пароль. Политика компании такова, что пароль
# должен содержать не менее 7 символов и обязательно включать первую букву имени
# (обязательно заглавную) и символ «”».

# def gen_pass(password, name):
#     if len(password) >= 7 and '"' in password and name[0].upper() in password:
#         return 'Пароль изменен!'
#     else:
#         return 'Пароль не соответствует требованиям компании'
#
#
# print(gen_pass('545"dsdsМ', 'Марк'))

###################################################################
# Задача 2. Программист, разрабатывающий
# приложение для хранения документов для архива, должен предусмотреть в приложении возможность вывода информации о
# документе в консоль.


# title = input('Введите заголовок: ')
# surname = input('Введите фамилию: ')
# name = input('Введите имя: ')
#
# print(title.upper(), surname.title(), name.title())
# ------------------------------------------------------------
# def document(title, name, type_of_document):
#     return title.upper(), name.title(), type_of_document.lower()
#
#
# title, name, type_doc = document(input('Введите заголовок '), input('Введите имя '), input('Введите тип документа '))
#
# print(title, '\n', name, '\n', type_doc)

########################################################################################
#
# def username (name, surname, patronymic):
#     login = surname + name[0] + patronymic[0]
#     return "Имя пользователя " + login + "@company.ru"
#
# # print (username ('Ivan', "Ivanov", "Ivanovich"))
#
# def pass_check (password, name):
#     if len(password) >=7 and '"' in password and name[0].upper() in password:
#         return "Пароль изменен!"
#     else : return "Пароль неверный!"
#
# name = input('Введите имя ')
# surname =  input('Введите фамилию ')
# patronymic = input('Введите отчество ')
#
# print(username (name, surname, patronymic))
# print (pass_check('379"оатк', name))

########################################################################################
# Кейс. Компания по продаже одежды разрабатывает каталог товаров и просит вас помочь в
# разработке. Необходимо создать приложение, которое:

def genery_art(tovar, country, price):
    art = (tovar + '_' + country[:3]).lower()
    return tovar.title(), art, str(price) + ' руб.'


print(genery_art(input('Введите название товара: '), input('Введите страну: '), int(input('Введите цену товара: '))))


# Магазин проводит акцию, вся одежда из Германии распродается со скидкой 20
# процентов. Необходимо проверить условие по стране производителя и изменять
# цену

# def catalog (name_of_good, country, price):
#     art = name_of_good.lower() +'_'+ country.lower()[:3]
#     if country == 'Германия':
#         price = price * 20 / 100
#     else:
#         price
#     return name_of_good.title(), art, price
# name, arti, price = catalog(input('Введите наименование товара '), input('Введите страну происхождения '), float(input('Введите цену ')))
# print(name, arti, price)