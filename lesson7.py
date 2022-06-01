########################################################################!!!
# Задача 1. Написать функцию, которая будет переводить градусы по фаренгейту в цельсии.

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


# print(f_to_c(100))
# print(round(f_to_c(100),2)) # 37.78

f100_in_celsius = f_to_c(100)


# print(f100_in_celsius) # 37.77777777777778

def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)  # 32.0


########################################################################!!!
# Задача 2. Определите функцию get_force, которая принимает массу и ускорение. Он должен вернуть массу, умноженную на ускорение.


# Функция принимает массу и ускорение
def get_force(mass, acceleration):
    return mass * acceleration


train_mass = 22680
train_acceleration = 10
rain_distance = 100
train_force = get_force(train_mass, train_acceleration)  # Возвращает нам массу, умноженную на ускорение.

print('Поезд GE поставляет ' + str(train_force) + ' ньютонов силы')  # Выводим результат массу, умноженную на ускорение.


# Функция принимает массу и "с" является постоянной величиной, которая обычно устанавливается на скорость света
def get_energy(mass, c=3 * 10 ** 8):
    return mass * c ** 2


bomb_mass = 1

bomb_energy = get_energy(bomb_mass)  # Получаем массу, умноженную на "c" в квадрате.
print('1 кг бомбы составляет ' + str(bomb_energy) + ' Джоулей')  # Выводим полученный результат в Джоулях


# Функция принимает массу, ускорение и расстояние.
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance  # Работа определяется как сила, умноженная на расстояние


train_work = get_work(train_mass, train_acceleration, rain_distance)

print('Поезд выполняет ' + str(train_work) + ' Джоулей за ' + str(rain_distance) + ' метров.')


########################################################################!!!
# Задача 3. Вернемся к задаче аналитика, который получил данные описательной статистики

def statistik(maximum, minimym, med, standart):
    if (maximum - med > 3 * standart) | (med - minimym < 3 * standart):
        return 'В ваших данных имеются выбросы и требуют предобработки'
    elif (maximum - med > 5 * standart) | (minimym - med < standart * 5):
        return 'В ваших данных имеются экстремальные значения и требуют предобработки'
    elif (maximum > med * 3) | (minimym < med * 3):
        return 'Ваши данные пригодны для анализа'
    else:
        pass


print(
    statistik(float(input('Введите максимум: ')),
              float(input('Введите минимум: ')),
              float(input('Введите среднее: ')),
              float(input('Стандартное отклонение: '))))


########################################################################!!!
# Задача 4. Вернемся к задаче из управления потоком про охранника Дмитрия и рекламное агентство

def check_task(user_name, arm_number):
    user_check = 'Добро пожаловать!'
    dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись ' \
                    'работой!'
    err_check = 'Логин и пароль не верный, попробуй  еще раз.'

    if user_name == 'Дмитрий' and arm_number != 1:
        return dmitriy_check
    elif user_name == 'Дмитрий' and arm_number == 1:
        return user_check
    elif user_name == 'Ангелина' and arm_number == 2:
        return user_check
    elif user_name == 'Василий' and arm_number == 3:
        return user_check
    elif user_name == 'Екатерина' and arm_number == 4:
        return user_check
    else:
        return err_check


print(check_task(input('Введите логин:  '), int(input('Введите АРМ:  '))))


########################################################################!!!
# Задача 5. Вернемся к задаче по управлению потоками

def med_ball(grade):
    if grade >= 4.0:
        return 'A'
    elif grade >= 3.0:
        return 'B'
    elif grade >= 2.0:
        return 'C'
    elif grade >= 1.0:
        return 'D'
    else:
        return 'F'


print(med_ball(float(input("Введите оценку: "))))

##################################################################################################
# # # - - - Работа со строками - - - # # #

my_fruit = 'blueberry'

length = len(my_fruit)

print(my_fruit[length - 1])  # y
print(my_fruit[-1])  # y, идентично [length-1]
print(my_fruit[length - 4:])  # erry
print(my_fruit[-4:])  # erry, идентично [length-4:]

print(my_fruit[4:9])  # Выведет berry, нужно указывать +1 к последнему символу.
print(my_fruit[4:])  # Выведет тоже самое berry, можно не указывать последнее число.
print(my_fruit[0:4])  # blue
print(my_fruit[:4])  # blue

####################################################################################
# Задание1. Вы программист, работаете в Island’s Limited Company

first_name = 'Джордж'
last_name = 'Вашингтон'

fixed_name = first_name[:4] + 'жж'
print(fixed_name)  # Джоржж

####################################################################################
# Задание. способ генерирации временных паролей для новых сотрудников.

first_name = 'Джордж'
last_name = 'Вашингтон'


def password_generator(f_name, l_name):
    temp_password = f_name[-3:] + l_name[-3:]
    return temp_password


print(password_generator(first_name, last_name))  # рджтон


def password_generator(f_name, l_name):
    temp_password = f_name[-2] + l_name[-2]
    return temp_password


print(password_generator(first_name, last_name))  # до, предпоследний символы

new_account = last_name[:5]
print(new_account)  # Вашин

temp_password = last_name[2:6]
print(temp_password)  # шинг


#########

def account_generator(f_name, l_name):
    new_account = f_name[:3] + l_name[:3]
    return new_account


print(account_generator(first_name, last_name))  # ДжоВаш

####################################################################################
fruit_prefix = "blue"
fruit_suffix = "berries"
fruit = fruit_prefix + '' + fruit_suffix
print(fruit)  # blueberries

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
print(favorite_fruit_conversation)  # He said, "blueberries are my favorite!" Экранируем строку!

"theycallme\"crazy\"91"  # Экранируем строку!

####################################################################################

word = "hello"


def print_letters(word):
    for a in word:  # letter можно назвать как угодно, word - переменная
        print(a)  # hello - выведет вертикально


print_letters(word)  # hello - выведет вертикально

####################################################################################
word = "hello ,23 "


def get_length(word):
    k = 0
    for i in word:
        k = k + 1  # k+=1 идентично
    return k


print(get_length(word))  # 10


def get_length1(word):
    k = 0
    for i in range(len(word)):
        k = k + 1  # k+=1 идентично
    return k


print(get_length1(word))  # 10
print(range(1, 10))  # range(1, 10), функция range передаёт целые числа от 1 до 9
print(range(9))  # функция range передаёт целые числа от 0 до 8


def get_length2(word):
    k = 0
    for i in range(len(word)):
        k = k + 1  # k+=1 идентично
    return k


print(get_length2(word))  # 10
print(range(1, 10))  # range(1, 10), функция range передаёт целые числа от 1 до 9
print(range(9))  # функция range передаёт целые числа от 0 до 8
