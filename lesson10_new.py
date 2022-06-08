###########################################################################
# - - - - - - - - - Занятие с Викторией Михайловной - - - - - - - - - - - #

string = 'КоТейка моя'
string2 = 'котейкА'
string = string.lower()  # котейка
string = string.upper()  # КОТЕЙКА
string = string.title()  # Котейка Моя

print(string.lower() == string2.lower())  # True
print(string)  # котейка
print(string.lower())  # котейка

###########################################################################
# Задание
# 1. Вы программист, работающий в организации, которая пытается оцифровать и
# хранить стихи под названием «Poetry Passion».
# Вам дали две строки, название стихотворения и его автора, и попросили их немного
# переформатировать, чтобы они соответствовали правилам базы данных организации.

poem_title = "евгений онегин"
poem_title_fixed = poem_title.title()
print(poem_title_fixed)

###########################################################################

black_cat = "Жил да был черный кот за углом"
black_cat = black_cat.split()  # ['Жил', 'да', 'был', 'черный', 'кот', 'за', 'углом']

print(black_cat)  # ['Жил', 'да', 'был', 'черный', 'кот', 'за', 'углом']

###########################################################################
# Задание
# 1. В переменной строка из первой строки стихотворения Ф.И. Тютчева «Весенние
# воды».
# Используйте .split (), чтобы создать список с именем line_one_words, который содержит
# каждое слово в этой строке стихов

line_one = "Еще в полях белеет снег"
line_one = line_one.split()
print(line_one)  # ['Еще', 'в', 'полях', 'белеет', 'снег']

###########################################################################
#
name = "santana"
print(name.split('n'))  # ['sa', 'ta', 'a']
print(name.split('a'))  # ['s', 'nt', 'n', '']

###########################################################################
# Задание
# 1. Ваш босс в прислал кучу имен авторов, которые он хочет, чтобы вы подготовили для
# импорта в базу данных. К сожалению, он отправил их в виде длинной строки с
# именами, разделенными запятыми

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, " \
          "Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni "
author_names = authors.split(', ')

# Создайте еще один список с именем author_last_names, который содержит только
# фамилии поэтов в предоставленной строке
author_last_names = []  # пустой список

for item in author_names:
    res = item.split()  # Разбиваем список
    author_last_names.append(res[-1])  # Метод append добавляет элемент в конец списка

print(
    author_names)  # ['Audre Lorde', 'William Williams', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kama la Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni ']

print(
    author_last_names)  # ['Lorde', 'Williams', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']

###########################################################################
#

smooth_chorus = \
    """And if you said, This life ain't good enough.
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')
print(
    chorus_lines)  # ['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"]

###########################################################################
# Задание
# 1. Организация прислала вам полный текст стихотворения Ф.И. Тютчева «Весенние
# воды». Они хотят, чтобы вы разбили стихотворение на отдельные строки.

spring_waters_text = \
    """ Еще в полях белеет снег,
А воды уж весной шумят —
Бегут и будят сонный брег,
Бегут, и блещут, и гласят…
Они гласят во все концы:
«Весна идет, весна идет,
Мы молодой весны гонцы,
Она нас выслала вперед!
Весна идет, весна идет,
И тихих, теплых майских дней
Румяный, светлый хоровод
Толпится весело за ней!..."""

spring_waters_lines = spring_waters_text.split(
    '\n')  # [' Еще в полях белеет снег,', 'А воды уж весной шумят —', 'Бегут и будят сонный брег,', 'Бегут, и блещут, и гласят… ', 'Они гласят во все концы:', '«Весна идет, весна идет,', 'Мы молодой весны гонцы,', 'Она нас выслала вперед! ', 'Весна идет, весна идет,', 'И тихих, теплых майских дней', 'Румяный, светлый хоровод', 'Толпится весело за ней!...']
print(spring_waters_lines)

###########################################################################
############## Соединение строк

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
result = ' '.join(my_munequita)  # My Spanish Harlem Mona Lisa
result = ', '.join(my_munequita)  # My, Spanish, Harlem, Mona, Lisa
result = ''.join(my_munequita)  # MySpanishHarlemMonaLisa
print(result)


###########################################################################
# Задача 1.
# Компания просит вас разработать приложение, которое позволит генерировать имя
# пользователей в системе, как конкатенацию имени и инициалов. Необходимо создать
# переменные:
# Name – содержит имя пользователя
# Surname – содержит фамилию пользователя
# Patronymic - содержит отчество.

def login_gen(name, surname, patronymic):
    login = surname + '.' + name[0] + patronymic[0]
    return login + '@company.ru'


print(login_gen('Mark', 'Fominykh', 'Viktorovikh'))

# Далее пользователю необходимо задать пароль. Политика компании такова, что пароль
# должен содержать не менее 7 символов и обязательно включать первую букву имени
# (обязательно заглавную) и символ «”»
password = input('Введите пароль из семи символов: ')  # M"fdgjp
name = input('Введите имя на латинице: ')  # Mark


def check_pass(password, name):
    if len(password) >= 7 and (name[0].title() in password) and ('"' in password):
        return 'Пароль изменен!'
    else:
        return 'Пароль не соответствует требованиям компании'


print(check_pass(password, name))


###########################################################################
# Задача 2.
# Программист, разрабатывающий приложение для хранения документов для архива,
# должен предусмотреть в приложении возможность вывода информации о документе в
# консоль.

def inf_doc(doc_name, name, last_name, doc_type):
    return doc_name.upper(), name.title(), last_name.title(), doc_type.lower()


document_name, author_name, author_last_name, document_type = inf_doc('Договор', 'Марк', 'Фоминых', 'юридический')

print(document_name, author_name, author_last_name, document_type)


###########################################################################
# Кейс.
# Компания по продаже одежды разрабатывает каталог товаров и просит вас помочь в
# разработке. Необходимо создать приложение, которое:
# • Генерирует артикул товара из названия товара и первых трех букв страны
# производителя, все буквы должны быть заглавные (артикул должен выглядеть,
# например, если переменная, характеризующая название товара хранит значение
# «Платье», а переменная для страны производителя содержит «Россия», то артикул:
# платье_рос).

#  Магазин проводит акцию, вся одежда из Германии распродается со скидкой 20
# процентов. Необходимо проверить условие по стране производителя и изменять
# цену.

def goods(product_name, country, price):
    articule = product_name + '_' + country[:3]
    if country.title() == 'Германия':
        price = price * 0.8

    return product_name.title(), articule.upper(), price


print(goods('платье', 'Германия', 100))


###########################################################################
# 1. Проверить имя
# Вы создаете приложение, которое позволяет пользователям взаимодействовать и делиться
# своими идеями проекта кодирования в Интернете. Первый шаг - указать свое имя в
# приложении и приветствовать других людей, в котором содержится ваше имя.

def check_name(string, name):
    if name.lower() in string.lower():
        return True
    else:
        return False


print(check_name('Hello, Ann!', 'ann'))

###########################################################################
# Сделать по 4-ю задачу в файле (Задания дополнительные_строки) занятия 10
