# Задача
donation = float(input('Введите донат: '))

if donation >= 1000:
    print("Спасибо вам за ваше пожертвование! Вы получили статус платинового пожертвования!")
elif donation >= 500:
    print("Спасибо вам за ваше пожертвование! Вы получили статус золотого пожертвования!")
elif donation >= 100:
    print("Спасибо вам за ваше пожертвование! Вы получили статус серебряного пожертвования!")
else:
 print("Спасибо вам за ваше пожертвование! Вы получили статус бронзового пожертвования!")
#
#
# # Задача
# a = 5
# b = 5
# try:
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("Can't")


# # Задача колл-центр
# mn1_busy = False
# mn2_busy = True
# mn3_busy = True
# head_mng = 'Главный менеджер'
#
# manager_num = 1
# queue = 3
#
# if mn1_busy == True and mn2_busy == True and mn3_busy == True and queue < 2:
#
# if mn1_busy == False and mn2_busy == False and mn3_busy == False:
#     mng_num = 1
#     print('Ваш менеджер: ', mng_num)
# #
# # if manager_num == True:
# #     print('Ваш менеджер 1')
# # elif manager_num == False and manager_num == 2 or manager_num == 3:
# #     print('Звонок отправляется второму')
# # elif manager_num == 1 and manager_num == 2
#
#
# manager_num_1=False
# manager_num_2=False
# manager_num_3=False
# #gl_manager
#
# # time=0
# ochered=2
#
# if (manager_num_1==True) and (manager_num_2==True) and (manager_num_3==True) | (manager_num_1==True) and (manager_num_2==True) and (manager_num_3==False) |(manager_num_1==True) and (manager_num_2==False) and (manager_num_3==False):
#     print('Ваш менеджер manager_num_1')
# elif (manager_num_1==False) and (manager_num_2==True) and (manager_num_3==True) |(manager_num_1==False) and (manager_num_2==True) and (manager_num_3==False):
#     print('Ваш менеджер manager_num_2')
# elif (manager_num_1==False) and (manager_num_2==False) and (manager_num_3==True) |(manager_num_1==True) and (manager_num_2==False) and (manager_num_3==True):
#     print('Ваш менеджер manager_num_3')
# elif ((manager_num_1==False) and (manager_num_2==False) and (manager_num_3==False)) and ochered<2:
#     print('Ожидайте ответа оператора')
# elif ((manager_num_1==False) and (manager_num_2==False) and (manager_num_3==False)) and ochered>=2:
#     print('Ваш менеджер gl_manager')


#
# auto_year = float(input("Возраст Вашего авто: "))
# volume = float(input("Объём Вашего авто: "))
# price = int(input("Стоимость Вашего авто: "))
# bet = 0

# if price < 8500:
#     resalt_calc = 2.5 * volume
# elif price >= 16700 and price < 42300:
#
# # Расчёт отчислений с учётом объёма двигателя
# if volume < 2.5:
#     resalt_calc_volume = 2.5 * volume
#
# if auto_year <= 2 and price <= 8500 and bet == 2.5:
#     print('Ставка ',bet + 'евро за 1 куб.')
# elif auto_year <= 2 and price > 8500 and price <= 16700 and bet == 2.5:
#     print('Ставка ',bet + 'евро за 1 куб.')
# elif auto_year <= 2 and price > 16700 and price <= 42300 and bet == 5.5:
#     print('Ставка ', bet + 'евро за 1 куб.')
# elif auto_year <= 2 and price > 42300 and price <= 84500 and bet == 7.5:
#     print('Ставка ', bet + 'евро за 1 куб.')
# elif auto_year <= 2 and price > 84500 and price <= 169000 and bet == 15:
#     print('Ставка ', bet + 'евро за 1 куб.')
# elif auto_year <= 2 and price > 169000 and bet == 20:
#     print('Ставка ', bet + 'евро за 1 куб.')


# ----------------------------------------------------------
# Таможенные отчисления
# Входные данные
# age = float(input('Возраст авто: '))
# volume = int(input('Объем двигателя (куб.см.): '))
# price = int(input('Цена авто (евро): '))
#
# # Основной расчет
# if age < 3:  # Расчёт для авто моложе 3-х лет
#     if price < 16700:
#         # bet=2.5
#         result_calc = 2.5 * volume
#     elif price >= 16700 and price < 42300:
#         # bet=5.5
#         result_calc = 5.5 * volume
#     elif price >= 42300 and price < 84500:
#         # bet=7.5
#         result_calc = 7.5 * volume
#     elif price >= 84500 and price < 169000:
#         # bet=15
#         result_calc = 15 * volume
#     else:
#         # bet=20
#         result_calc = 20 * volume
#         # result_calc = volume * bet
#     print('Таможенные отчисления на ваш автомобиль составят: ', result_calc)
# elif age >= 3 and age <= 5:
#     if volume < 1000:
#         # bet=1.5
#         result_calc = 1.5 * volume
#     elif volume >= 1000 and volume < 1500:
#         # bet=1.7
#         result_calc = 1.7 * volume
#     elif volume >= 1500 and volume < 1800:
#         # bet=2.5
#         result_calc = 2.5 * volume
#     elif volume >= 1800 and volume < 2300:
#         # bet=2.7
#         result_calc = 2.7 * volume
#     elif volume >= 2300 and volume < 3000:
#         # bet=3
#         result_calc = 3 * volume
#     else:
#         # bet=3.6
#         result_calc = 3.6 * volume
#         # result_calc = volume * bet
#     print('Таможенные отчисления на ваш автомобиль составят: ', result_calc)
# else:pass
# ----------------------------------------------------------
































