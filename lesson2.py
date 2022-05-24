# Со второго урока
#message_string = "Hello there"
message_string = 9  # Коментируем строоку
message_string = "Привет мир!"

# Со второго урока
a = 54
print(a * 5 / 7)  # 38.57142857142857
print(a * 5 // 7)  # 38
print(a * 5 % 7)  # 4

# Со второго урока
a = 23
b = 13
c = a * b
print("Площадь треугольника равна:", c)  # 299

# Со второго урока
a = 8
b = 12
c1 = a * b
b = 8
c = a * b
print("Площадь одеяла равна %s лоскутков, а старая площадь была %s" % (c, c1))

# Самостоятельное задание
Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price * Oil_work_time  # Замена масла
Oil_price = 700 * 1.05  # Масло
Filtr_work = 450 * 0.5  # Замена воздушного фильтра
Filtr_price = 300 * 1.05  # Воздушный фильтр
Cost_sum = Oil_work_cost + Oil_price + Filtr_work + Filtr_price  # Итого
sale = Cost_sum * 0.03  # Персональная скидка 3%
Net_sum_cost = Cost_sum - (Cost_sum * 0.03)  # Итого с учетом скидки

print('''
      Расчет работ по представленному автомобилю:
          Замена масла (работы): %s руб.
          Масло Castrol: %s руб.
          Замена воздушного фильтра: %s руб.
          Воздушный фильтр: %s руб.
          Итого: %s руб.
          Персональная скидка 3%%: %s руб.
          Итого с учетом скидки: %s руб.
      ''' % (Oil_work_cost, Oil_price, Filtr_work, Filtr_price, Cost_sum, sale, Net_sum_cost))
