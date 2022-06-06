def electric(t1, t2, t3):
    result_electro = (t1 * 6.18) + (t3 * 5.15) + (t2 * 1.74)
    return 'Сумма оплаты за электроэнергию составила: ', result_electro


def gas(t1, t2, t3):
    result_gas = (t1 * 6.18) + (t3 * 5.92) + (t2 * 7.10)
    return 'Сумма оплаты за электроэнергию составила: ', result_gas


t1 = float(input('Введите показания по Тарифу 1 = '))
t2 = float(input('Введите показания по Тарифу 2 = '))
t3 = float(input('Введите показания по Тарифу 3 = '))
stove = input('Какая у Вас плита газ / электро?: ')

if stove == 'газ':
    result = gas(t1, t2, t3)
elif stove == 'электро':
    result = electric(t1, t2, t3)

print(result)