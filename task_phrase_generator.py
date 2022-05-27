# Генератор фраз
# Вариант для 1 колонки
col1_row1 = 'Коллеги, '
col1_row2 = 'В то же время, '
col1_row3 = 'Однако, '
col1_row4 = 'Тем не менее, '
col1_row5 = 'Следовательно, '
col1_row6 = 'Соответственно, '
col1_row7 = 'Вместе с тем, '
col1_row8 = 'С другой стороны, '

# Вариант для 2 колонки
col2_row1 = 'парадигма цифровой экономики '
col2_row2 = 'контекст цифровой трансформации '
col2_row3 = 'диджитализация бизнес-процессов '
col2_row4 = 'парагматичный подход к цифровым платформам '
col2_row5 = 'совокупность сквозных технологий '
col2_row6 = 'программа прорывных исследований '
col2_row7 = 'ускорение блокчейн-транзакций '
col2_row8 = 'экспоненциальный рост Big Data '

# Вариант для 3 колонки
col3_row1 = 'открывает новые возможности для '
col3_row2 = 'выдвигает новые требования '
col3_row3 = 'несет в себе риски '
col3_row4 = 'расширяет горизонты '
col3_row5 = 'заставляет искать варианты '
col3_row6 = 'не оставляет шанса для '
col3_row7 = 'повышвет вероятность '
col3_row8 = 'обостряет проблему '

# Вариант для 4 колонки
col4_row1 = 'дальнейшего углубления '
col4_row2 = 'бюджетного финансирования '
col4_row3 = 'синергетического эффекта '
col4_row4 = 'компроментации конфидециальных '
col4_row5 = 'универсальной коммодитизации '
col4_row6 = 'нессанкционированной кастомизации '
col4_row7 = 'нормативного регулирования '
col4_row8 = 'практического применения '

# Вариант для 5 колонки
col5_row1 = 'знаний и компененций.'
col5_row2 = 'непроверенных гипотез.'
col5_row3 = 'волатильных активов.'
col5_row4 = 'опасных экспериментов.'
col5_row5 = 'государственно-частных партнёрств.'
col5_row6 = 'цифровых следов граждан.'
col5_row7 = 'нежелательных последствий.'
col5_row8 = 'внезапных открытий.'

import random  # Импортируем random

# Подбираем номер ячейки случайным образом для каждого столбца таблицы
random_col1 = random.randint(1, 8)
random_col2 = random.randint(1, 8)
random_col3 = random.randint(1, 8)
random_col4 = random.randint(1, 8)
random_col5 = random.randint(1, 8)

# Проверяем сгененрированное число для 1 столбца и вводим переменную, которая будут принимать текст из соотвествующей ячейки
if random_col1 == 1:
    text1 = col1_row1
elif random_col1 == 2:
    text1 = col1_row2
elif random_col1 == 3:
    text1 = col1_row3
elif random_col1 == 4:
    text1 = col1_row4
elif random_col1 == 5:
    text1 = col1_row5
elif random_col1 == 6:
    text1 = col1_row6
elif random_col1 == 7:
    text1 = col1_row7
elif random_col1 == 8:
    text1 = col1_row8

# Проверяем сгененрированное число для 2 столбца и вводим переменную, которая будут принимать текст из соотвествующей ячейки
if random_col2 == 1:
    text2 = col2_row1
elif random_col2 == 2:
    text2 = col2_row2
elif random_col2 == 3:
    text2 = col2_row3
elif random_col2 == 4:
    text2 = col2_row4
elif random_col2 == 5:
    text2 = col2_row5
elif random_col2 == 6:
    text2 = col2_row6
elif random_col2 == 7:
    text2 = col2_row7
elif random_col2 == 8:
    text2 = col2_row8

# Проверяем сгененрированное число для 3 столбца и вводим переменную, которая будут принимать текст из соотвествующей ячейки
if random_col3 == 1:
    text3 = col3_row1
elif random_col3 == 2:
    text3 = col3_row2
elif random_col3 == 3:
    text3 = col3_row3
elif random_col3 == 4:
    text3 = col3_row4
elif random_col3 == 5:
    text3 = col3_row5
elif random_col3 == 6:
    text3 = col3_row6
elif random_col3 == 7:
    text3 = col3_row7
elif random_col3 == 8:
    text3 = col3_row8

# Проверяем сгененрированное число для 4 столбца и вводим переменную, которая будут принимать текст из соотвествующей ячейки
if random_col4 == 1:
    text4 = col4_row1
elif random_col4 == 2:
    text4 = col4_row2
elif random_col4 == 3:
    text4 = col4_row3
elif random_col4 == 4:
    text4 = col4_row4
elif random_col4 == 5:
    text4 = col4_row5
elif random_col4 == 6:
    text4 = col4_row6
elif random_col4 == 7:
    text4 = col4_row7
elif random_col4 == 8:
    text4 = col4_row8

# Проверяем сгененрированное число для 5 столбца и вводим переменную, которая будут принимать текст из соотвествующей ячейки
if random_col5 == 1:
    text5 = col5_row1
elif random_col5 == 2:
    text5 = col5_row2
elif random_col5 == 3:
    text5 = col5_row3
elif random_col5 == 4:
    text5 = col5_row4
elif random_col5 == 5:
    text5 = col5_row5
elif random_col5 == 6:
    text5 = col5_row6
elif random_col5 == 7:
    text5 = col5_row7
elif random_col5 == 8:
    text5 = col5_row8

print('Подбор случайных слов из 5 колонок: ', text1, text2, text3, text4, text5)