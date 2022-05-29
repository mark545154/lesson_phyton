# Задача 6. Необходимо выбрать, какое число из трех входных значений является наибольшим, используя условные операторы.
def result(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return 'Число 1 больше чем два других числа ', num1
    elif num2 > num1 and num2 > num3:
        return 'Число 2 больше чем два других числа ', num2
    elif num3 > num1 and num3 > num2:
        return 'Число 3 больше чем два других числа', num3
    else:
        return 'Ничья!'

print (result (int(input('Число 1: ')),int(input('Число 2: ')), int(input('Число 3: '))))