import random

random_list = [random.randint(1, 20) for i in range(20)]  # формируем список чисел (список игроков)]
num = random.randint(1, 9)  # формируем загаданное число от 1 до 9


# не нужно. рандинт возвращает число. num_str = str(num)  # переводим число в строку

def sum_od(n, rand_list):  # передаём загаданное число и кол-во игроков
    priz_num = []
    for num in rand_list:
        x = num % 10
        y = num // 10
        if (x + y) % n == 0:
            priz_num.append(num)
    return priz_num


print(num)
print(sum_od(num, random_list))
