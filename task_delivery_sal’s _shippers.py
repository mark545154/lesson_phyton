# Задача 3. Доставка Сала

dilevery = input('Как вы хотите отправить посылку? (Курьером-1), (Дроном-2): ')
ves = int(input('Введите вес посылки в фунтах: '))

if dilevery == '1':  # Доставка курьером
    if ves <= 2:
        price = ves * 1.5 + 20
    elif 2 > ves <= 6:
        price = ves * 3 + 20
    elif 6 > ves <= 10:
        price = ves * 4 + 20
    elif ves > 10:
        price = ves * 4.75 + 20
    print('Доставка курьером будет стоить: ', price)

elif dilevery == '2':  # Доставка дроном
    if ves <= 2:
        price = ves * 4.5
    elif 2 > ves <= 6:
        price = ves * 9
    elif 6 > ves <= 10:
        price = ves * 12
    elif ves > 10:
        price = ves * 14.25
    print('Доставка дроном будет стоить: ', price)