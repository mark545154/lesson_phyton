gas = input('Оборудовано газовой плитой? да/нет: ')

T1 = float(input('T1 = '))
T2 = float(input('T2 = '))
T3 = float(input('T3 = '))
if gas == 'да':
    result_calc = T1 * 6.18 + T3 * 5.92 + T2 * 7.10
else:
    result_calc = T1 * 6.18 + T3 * 5.15 + T2 * 1.74
print(result_calc)
