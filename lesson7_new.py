########################################################################!!!
# Задача 1. Написать функцию, которая будет переводить градусы по фаренгейту в цельсий

# def f_to_c(f_temp = float(input('Введите значение температуры F: '))):
#     c_temp = (f_temp - 32) * 5 / 9
#     return int(round(c_temp, 0)) # int(round()), округляем до целого числа
#
# f100_in_celsius = f_to_c()
# print('Градус цельсия будет: ', f100_in_celsius)
#
# # Работа в обратную сторону
#
# def c_to_f(c_temp):
#     f_temp = c_temp * 9 / 5 + 32
#     return int(round(f_temp, 0)) # int(round()), округляем до целого числа
#
# c0_in_fahrenheit = c_to_f(f_to_c(50)) # Принимаем значение верхней функции f_to_c()
#
# # c0_in_fahrenheit = c_to_f(float(input('Введите значение температуры C: ')))
#
# print('Градус фаренгейта будет: ', c0_in_fahrenheit)


########################################################################!!!
# Задача 2. Определите функцию get_force, которая принимает массу и ускорение

# def get_force(mass, acceleration):
#     return mass * acceleration
#
#
# train_mass = 22680
# train_acceleration = 10
# rain_distance = 100
# train_force = get_force(train_mass, train_acceleration)
#
# print('Поезд GE поставляет ' + str(train_force) + ' ньютонов силы')
#
#
# def get_energy(mass, c=3 * 10 ** 8):
#     return mass * c ** 2
#
#
# bomb_mass = 1
#
# bomb_energy = get_energy(bomb_mass)
# print('1 кг бомбы составляет ' + str(bomb_energy) + ' Джоулей')
#
#
# def get_work(mass, acceleration, distance):
#     force = get_force(mass, acceleration)
#     return force * distance
#
#
# train_work = get_work(train_mass, train_acceleration, rain_distance)
#
# print('Поезд выполняет ' + str(train_work) + ' Джоулей за ' + str(rain_distance) + ' метров.')

########################################################################!!!
# Задача 3. Вернемся к задаче аналитика, который получил данные описательной статистики

# def analytic(maxy, med, miny, standart):
#     if maxy - med > 5 * standart or med - miny > 5 * standart:
#         return 'В ваших данных имеются экстремальные значения и требуют предобработки'
#     elif maxy - med > 3 * standart or med - miny > 3 * standart:
#         return 'В ваших данных имеются выбросы и требуют предобработки'
#     else:
#         return 'Ваши данные пригодны для анализа'
#
#
# print(analytic(float(input('Введите максимум: ')),
#                float(input('Введите среднее: ')),
#                float(input('Введите минимум: ')),
#                float(input('Введите cтандартное: '))))


########################################################################!!!
# Задача 4. Вернемся к задаче из управления потоком про охранника Дмитрия и рекламное агентство.

# user_name = str(input('Введите логин:  '))
# arm_number = int(input('Введите № АРМ:  '))

# def check_task(user_name, arm_number):
#
#     user_check = 'Добро пожаловать!'
#     dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись ' \
#                     'работой!'
#     err_check = 'Логин и пароль не верный, попробуй  еще раз.'
#
#     if user_name == 'Дмитрий' and arm_number != 1:
#         return dmitriy_check
#     elif user_name == 'Дмитрий' and arm_number == 1:
#         return user_check
#     elif user_name == 'Ангелина' and arm_number == 2:
#         return user_check
#     elif user_name == 'Василий' and arm_number == 3:
#         return user_check
#     elif user_name == 'Екатерина' and arm_number == 4:
#         return user_check
#     else:
#         return err_check
#
# print(check_task(input('Введите логин:  '), int(input('Введите № АРМ:  '))))

########################################################################!!!
# Задача 5. Вернемся к задаче по управлению потоками

# def med_ball(grade):
#     if grade >= 4.0:
#         return 'A'
#     elif grade >= 3.0:
#         return 'B'
#     elif grade >= 2.0:
#         return 'C'
#     elif grade >= 1.0:
#         return 'D'
#     else:
#         return 'F'
#
#
# print(med_ball(int(input("Введите оценку: "))))

########################################################################!!!
# # # - - - Работа со строками - - - # # #
# My_fruit = "blueberry"
#
# print(My_fruit[2])  # u
# print(My_fruit[-2])  # r
#
# print(My_fruit[0:5])  # blueb
# print(My_fruit[:5])  # blueb, тоже самое что и выше
#
# print(My_fruit[1:])  # lueberry
# print(My_fruit[0:])  # blueberry

# My_fruit[3] = 'u' # Не заменит, так как строка имутабельна

########################################################################!!!
# Задание1. Вы программист, работаете в Island’s Limited Company
last_name = 'Вашингтон'

new_account = last_name[:5]  # Вашин
new_account = last_name[2] + last_name[5]  # шг
# new_account = last_name[2:6]  # шинг
print(new_account)
########################################################################
#
