###################################################################
#

stroka1 = 'HEllo'
stroka2 = stroka1.lower()

print(stroka2)  # hello
print(stroka1.lower())  # hello
print(stroka1.upper())  # HELLO
print(stroka1.title())  # Hello

###################################################################
# Задание1. Вы программист, работающий в организации, которая пытается оцифровать и хранить стихи под названием «Poetry Passion».

poem_title = "евгений онегин"
poem_author = "Александр Сергеевич Пушкин"

poem_title_fixed = poem_title.title()
print(poem_title)  # евгений онегин
print(poem_title_fixed)  # Евгений Онегин

###################################################################
#

poem_title = "евгений онегин"
poem_author = "Александр, Сергеевич, Пушкин"

print(poem_author.split(', '))  # ['Александр', 'Сергеевич', 'Пушкин']

###################################################################
# Задание1. В переменной строка из первой строки стихотворения Ф.И. Тютчева «Весенние воды».

line_one = "Еще в полях белеет снег"
line_one_words = line_one.split()
print(line_one_words)  # ['Еще', 'в', 'полях', 'белеет', 'снег']

###################################################################
# Задание. Ваш босс в прислал кучу имен авторов, которые он хочет, чтобы вы подготовили для импорта в базу данных

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kama la Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(', ')
print(
    author_names)  # ['Audre Lorde', 'William Carlos Williams', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kama la Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']

# 3. Создайте еще один список с именем author_last_names, который содержит только фамилии поэтов в предоставленной
# строке.
author_last_names = []  # Объявляем переменную чтобы сделать список
for author in author_names:  # Для каждого элемента author_names
    author_last_names = author.split()[-1]  # разделяем имя и фамилию списка и берём только фамилию

    print(author_last_names)  # Lorde
    # Williams
    # Mistral
    # Toomer
    # Qi
    # Whitman
    # Silverstein
    # Boullosa
    # Suraiyya
    # Hughes
    # Rich
    # Giovanni

###################################################################
#
smooth_chorus = \
    """And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')
print(chorus_lines)

new_chorus = ' '.join(chorus_lines)  # Метод join() объединяет! Противоположный split()
print(new_chorus)

###################################################################
# Задание1. Организация прислала вам полный текст стихотворения Ф.И. Тютчева «Весенние воды». Они хотят, чтобы вы разбили стихотворение на отдельные строки.

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

spring_waters_lines = spring_waters_text.split('\n')
print(spring_waters_lines)

###################################################################
# .join()

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))  # My Spanish Harlem Mona Lisa


###################################################################
# Задача 1. Компания просит вас разработать приложение, которое позволит генерировать имя пользователей в системе, как конкатенацию имени и инициалов. Необходимо создать переменные


def genery(surname, name, patronymic):
    login = surname + name[0] + patronymic[0]
    return 'Имя пользователя ' + login + '@company.ru'


print(genery('Имя', 'Фамилия', 'Отчество'))


# Далее пользователю необходимо задать пароль. Политика компании такова, что пароль
# должен содержать не менее 7 символов и обязательно включать первую букву имени
# (обязательно заглавную) и символ «”».

def gen_pass(password, name):
    if len(password) >= 7 and '"' in password and name[0].upper() in password:
        return 'Пароль изменен!'
    else:
        return 'Пароль не соответствует требованиям компании'


print(gen_pass('545"dsdsМ', 'Марк'))

###################################################################
# Задача 2. Программист, разрабатывающий
# приложение для хранения документов для архива, должен предусмотреть в приложении возможность вывода информации о
# документе в консоль.


title = input('Введите заголовок: ')
surname = input('Введите фамилию: ')
name = input('Введите имя: ')

print(title.upper(), surname.title(), name.title())


##############################################################

def document(title, name, type_of_document):
    return title.upper(), name.title(), type_of_document.lower()


title, name, type_doc = document(input('Введите заголовок '), input('Введите имя '), input('Введите тип документа '))

print(title, '\n', name, '\n', type_doc)


########################################################################################
#
def username(name, surname, patronymic):
    login = surname + name[0] + patronymic[0]
    return "Имя пользователя " + login + "@company.ru"


# print (username ('Ivan', "Ivanov", "Ivanovich"))

def pass_check(password, name):
    if len(password) >= 7 and '"' in password and name[0].upper() in password:
        return "Пароль изменен!"
    else:
        return "Пароль неверный!"


name = input('Введите имя на латинице: ')
surname = input('Введите фамилию на латинице: ')
patronymic = input('Введите отчество на латинице: ')

print(username(name, surname, patronymic))
print(pass_check(input('Введите пароль чтобы содержал 1-ю заглавную букву имени и ": '), name.title()))


########################################################################################
# Кейс. Компания по продаже одежды разрабатывает каталог товаров и просит вас помочь в
# разработке. Необходимо создать приложение, которое:

def genery_art(tovar, country, price):
    art = (tovar + '_' + country[:3]).lower()

    # Магазин проводит акцию, вся одежда из Германии распродается со скидкой 20
    # процентов. Необходимо проверить условие по стране производителя и изменять
    # цену
    if country.title() == 'Германия' or country.title() == 'Germany':
        sale_price = price * 0.8
        return tovar.title(), art, str(sale_price) + ' руб.'

    return tovar.title(), art, str(price) + ' руб.'


print(genery_art(input('Введите название товара: '), input('Введите страну: '), int(input('Введите цену товара: '))))


#############################################################################
# 2. Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
#
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод.

def result_dnk(dnk):  # Объявляем функцию
    res = str()  # переводим результат в строку
    dnk = dnk + '1'  # Переопределяем переменную
    num = dnk[0]  # берём первый символ и перезаписываем в новую переменную
    i = 0  # Определяем временную переменную со значением 0
    for r in dnk:  # Проверяем циклом for длину введённой переменной
        if num != r:  # Проверяем чтобы наш символ num не равен переменной r
            res += num + str(i)  # Прибавляем и записываем результаты прибавления переменной i
            num = r  # Записываем результат r в переменную num
            i = 0  # Присваиваем переменной значение 0
        i += 1  # Прибавляем переменную i на единицу
    return res.lower()  # a4b2c1a2


print(result_dnk(dnk='AAAAbbCaa'.lower()))


#############################################################################
# 1. Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
#
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
#
# Важно! На вход программе подаётся строка из шести цифр.

def chek_result(ticket):
    ticket = [int(i) for i in ticket]
    if sum(ticket[:-3]) == sum(ticket[3:]):
        return 'Счастливый'
    else:
        return 'Обычный'


print(chek_result(input('Введите номер билета из 6 цифр: ')))
