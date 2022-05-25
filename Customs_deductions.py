# Таможенные отчисления

age = float(input('Возраст авто: '))
volume = int(input('Объем двигателя (куб.см.): '))
price = int(input('Цена авто (евро): '))

# Основной расчет
if age < 3:  # Расчёт для авто моложе 3-х лет
    if price < 16700:
        bet = 2.5
    elif price >= 16700 and price < 42300:
        bet = 5.5
    elif price >= 42300 and price < 84500:
        bet = 7.5
    elif price >= 84500 and price < 169000:
        bet = 15
    else:
        bet = 20
    result_calc = volume * bet
    print('Таможенные отчисления на ваш автомобиль составят: ', result_calc)

elif age >= 3 and age <= 5:
    if volume < 1000:
        bet = 1.5
    elif volume >= 1000 and volume < 1500:
        bet = 1.7
    elif volume >= 1500 and volume < 1800:
        bet = 2.5
    elif volume >= 1800 and volume < 2300:
        bet = 2.7
    elif volume >= 2300 and volume < 3000:
        bet = 3
    else:
        bet = 3.6
    result_calc = volume * bet
    print('Таможенные отчисления на ваш автомобиль составят: ', result_calc)
else: pass