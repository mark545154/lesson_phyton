print((5 * 2) - 1 == 8 + 1)  # True
print(13 - 6 != (3 * 2) + 1) # False
print(3 * (2 - 1) == 4 - 1)  # True


my_baby_bool = True   #<class 'bool'>
my_baby_bool = 'true' #<class 'str'>
print (type(my_baby_bool)) 


# Проверка условий
if 2 == 4 - 2:
    print("apple")
    
print('Hello') # Неявляется условием if, так как находиться на другом уровне


# Задание 1
enter_number = 3
arm = 1
user_name = 'Ангелина'

dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
user_check = 'Добро пожаловать!'
error_message = 'Логин или пароль не верный, попробуйте ещё раз'

if ((user_name == 'Дмитрий') & (arm == 1)) | ((user_name == 'Ангелина') & (arm == 2)):
    print(user_check)

elif (user_name == 'Дмитрий') & (arm != 1):
    print(dmitriy_check)
    
elif (user_name == 'Ангелина') & (arm != 2) & (enter_number <= 3):
    print(error_message)



# if user_name == 'Дмитрий':
#     print(dmitriy_check)
# else:
#     print(user_check)



# Задание 2. or и | идентичны и могут быть взаимозаменяемы, проверка выражений
print((2 - 1 > 3) or (-5 * 2 == -10)) # True
print((9 + 5 <= 15) | (7 != 4 + 3))   # True


# Задание 3
enter_number = 4

if enter_number <= 3:
    print('Попробуйте еще раз. У вас осталось ' + str(enter_number) + ' попыток')
else:
    print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки')


# Задание 4. and и & идентичны, проверка выражений
print((2 + 2 + 2 >= 6) and (-1 * -1 < 0)) # False
print((4 * 2 <= 8) & (7 - 1 == 6)) # True



# Самостоятельная задача на странице 9 (про грейды и университет)
grade = 0.0

if grade >= 4.0:
    print("A")
elif grade >= 3.0:
    print("B")
elif grade >= 2.0:
    print("C")
elif grade >= 1.0:
    print("D")
else:
    print("F")


# Из лабораторной работы 2 по управлению потоками делаете задачу номер 1
grade_hall = 4

if grade_hall < 2:
    print("Вам необходимо пройти в малый зал")
elif grade_hall == 2:
    print("Вам необходимо пройти в большой зал")
elif grade_hall >= 3:
    print("Вам необходимо пройти в тренажерный зал")
else:
    print("Укажите номер Вашего курса!")
    


# 
manager_num = 1 # номер менеджера! В колл-центре всего 4 менеджера отвечающего на звонки и старший менеджер












