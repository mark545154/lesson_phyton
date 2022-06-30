# 4. Имеются данные о продажах некоторого магазина:
# Товары, которые продавала аптека на неделе:
# Картон (300 руб, купили 10 раз),
# Бумага (500 руб, купили 6 раз),
# Ножницы (124 руб, купили 12 раз),
# Папка (750 руб, купили 4 раза),
# Набор профессиональной акварели (567 руб, купили 5 раз),
# Подставка-котик (320 руб., купили 20 раз).
# Необходимо создать файл csv, который содержит название товара,
# стоимость и количество покупок,
# разработать приложение (использовать словари),
# чтобы на выходе можно было получить средние количество продаж,
# выручке, ценах, а также максимальное и минимальное значение,
# самый продаваемый товар, самый непопулярный товар.
# Всю статистику необходимо вывести в консоль и сохранить в отдельный файл.

import csv

# Создаём список который в дальнейшем запишем в файл csv
product_list = [{'name': 'Картон', 'price': 300, 'purchases': 10},
                {'name': 'Бумага', 'price': 500, 'purchases': 6},
                {'name': 'Ножницы', 'price': 124, 'purchases': 12},
                {'name': 'Папка', 'price': 750, 'purchases': 4},
                {'name': 'Набор профессиональной акварели', 'price': 567, 'purchases': 5},
                {'name': 'Подставка-котик', 'price': 320, 'purchases': 20}]

# Создаём и записываем в файл csv
with open('sales.csv', 'w', encoding='UTF-8') as sal_csv:
    fields = ['name', 'price', 'purchases']  # Заголовок scv файла
    record = csv.DictWriter(sal_csv, fieldnames=fields)
    record.writeheader()  # Записываем всё в header

    # Перебираем список и записываем
    for index in product_list:
        record.writerow(index)
sal_csv.close()  # закрываем csv файл с которым работали


# Функция, которая обрабатывает файл csv и возвращает список
def file_loading(file_name, delim, column):
    result = []  # Пустой список для записи в него значения
    new_product_list = []  # Создаём для обработки в цикле for
    new_product_list_2 = []  # Создаём для обработки в цикле for
    with open(file_name) as file_csv:
        file_reader = csv.DictReader(file_csv, delimiter=delim)
        for row in file_reader:
            result.append(float(row[column]))
            new_product_list.append(row)  # В этот лист будут добавлены строковые значения из файла csv,
            # которые в дальнейшем прогоним через цикл for самый не популярный товар
            new_product_list_2.append(row)  # В этот лист будут добавлены строковые значения из файла csv,
            # которые в дальнейшем прогоним через цикл for самый популярный товар
    return result, new_product_list, new_product_list_2


# Объявляем переменные которые будут передаваться в функцию sals(price_sale, quantity)
# Переменную sale_product и sale_product_2 прогоняем по двум циклам for, для определения
# самый продаваемый товар и самый непопулярный товар.
# price_product и price_x не задействована, без неё выбивает ошибку
quantity, sale_product, sale_product_2 = file_loading('sales.csv', ',', 'purchases')
price_sale, price_product, price_x = file_loading('sales.csv', ',', 'price')

# Объявляем переменную, которой достаём кол-во продаж из файла scv
no_pop = sale_product[1]
# Проверяем циклом самый не популярный товар
for i in range(len(sale_product)):
    if float(sale_product[i]['purchases']) < float(no_pop['purchases']):
        no_pop['price'] = float(sale_product[i]['price'])
        no_pop['purchases'] = float(sale_product[i]['purchases'])
        no_pop['name'] = sale_product[i]['name']

# Объявляем переменную, которой достаём кол-во продаж из файла scv
pop_pro = sale_product_2[i]
# Этот цикл проверяет самый популярный товар по продажам
for index in range(len(sale_product_2)):
    if float(sale_product_2[index]['purchases']) > float(pop_pro['purchases']):
        pop_pro['price'] = float(sale_product_2[index]['price'])
        pop_pro['purchases'] = float(sale_product_2[index]['purchases'])
        pop_pro['name'] = sale_product_2[index]['name']


# Функция прогоняет и определяет значения, которые прописаны в функции
def sals(price_list, sale_list):
    # Находим среднее в кол-ве продаж в списке purchases
    ave_sale = sum(sale_list) / len(sale_list)
    # Находим среднюю цену в листе price
    ave_price = sum(price_list) / len(price_list)

    # Находим максимальное значение в списке purchases
    max_sale = max(sale_list)
    # Находим максимальное значение в списке price
    max_price = max(price_list)

    # Находим минимальное значение в списке purchases
    min_sale = min(sale_list)
    # Находим минимальное значение в списке price
    min_price = min(price_list)

    # Среднее кол-во продаж за 10 дней
    revenue = [(price_list[i]) * sale_list[i] / 10 for i in range(len(sale_list))]
    sor_rev = sorted(revenue)
    return ave_sale, (round(ave_price), 1), max_sale, max_price, min_sale, min_price, sor_rev


ave_sale, ave_price, max_sale, max_price, min_sale, min_price, sor_rev = sals(price_sale, quantity)

# Выводим в консоль результаты
print(f'''За неделю:
Среднее значение по продажам {ave_sale}
Среднее значение по цене {ave_price}
Максимальное кол-во товаров продано {max_sale}
Максимальная продажа по цене {max_price}
Минимальное кол-во которое было продано {min_sale}
Минимальная цена по продажам {min_price}
Средняя выручка за 7 дней {sor_rev}
Самый продаваемый товар {pop_pro}
Самый непопулярный товар {no_pop}''')

# Создаём файл txt и записываем в него полученные данные
with open('new_sales.txt', 'a', encoding='UTF-8') as n_sals:
    n_sals.write(f'''За неделю:
    Среднее значение по продажам {ave_sale}
    Среднее значение по цене {ave_price}
    Максимальное кол-во товаров продано {max_sale}
    Максимальная продажа по цене {max_price}
    Минимальное кол-во которое было продано {min_sale}
    Минимальная цена по продажам {min_price}
    Средняя выручка за 7 дней {sor_rev}
    Самый продаваемый товар {pop_pro}
    Самый непопулярный товар {no_pop}''')

# Закрываем файл в который записали полученные значения
n_sals.close()
