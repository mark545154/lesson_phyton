###################################################################################
#
# Задание
# 1. Определите три списка, x, y1 и y2, и заполните их целыми числами. Эти числа могут
# быть чем угодно, но было бы неплохо, если бы они были фактическими
# показателями, которые вы хотите сравнивать. Данные можно посмотреть на этом
# сайте: http://www.tylervigen.com/spurious-correlations
# 2. Постройте график зависимости y1 и x и отобразите график.
# 3. На том же графике постройте y2 vs x (после линии, где вы строите y1 vs x)
# 4. Сделайте линию y1 розовой линией, а линию y2 серой линией. Дайте обеим линиям
# круглые маркеры.
# 5. Дайте своему графику название «Две линии на одном графике», а ось X -
# «Великолепная ось X», а ось Y - «Потрясающая ось Y».
# 6. Создайте для графика легенду и поместите ее в правом нижнем углу.
# 7. Попробуйте применить различные методы, изученные в данном разделе. Может
# быть, сделайте какие-нибудь подграфики и разделите линии. Потренируйтесь с
# увеличением определенных частей графика или выбором определенных x- или y отметок для отображения

from matplotlib import pyplot as plt

plt.figure(figsize=(10, 9))  # создаём новую фигуру со своими размерами  figsize = (width, height)

x = [2018, 2019, 2020, 2021, 2022]
y1 = [102, 106, 110, 114, 118]
y2 = [105.2, 104.26, 102.31, 105.67, 117.83]

ax = plt.subplot(3, 1, 1)
ax.set_xticks([2018, 2019, 2020, 2021, 2022])
ax.set_xticklabels(['2018 год', '2019 год', '2020 год', '2021 год', '2022 год'])
ax.set_yticks([102, 106, 110, 114, 118])
ax.set_yticklabels(['102%', '106%', '110%', '114%', '118%'])
plt.plot(x, y1)
plt.subplots_adjust(hspace=0.1, left=0.15, right=0.95, bottom=0, wspace=0.1)
plt.title('Индексы потребительских цен на товары и услуги по РФ\n "Две линии на одном графике"', fontsize=10, fontweight="bold", color='#008080')
plt.xlabel('К соответствующему месяцу предыдущего года\n"Великолепная ось X"', fontsize=8, fontweight="bold", color='red')
plt.ylabel('Процент\n"Потрясающая ось Y"', fontsize=8, fontweight="bold", color='blue')
plt.plot(x, y1, color='#ffc0cb', marker='o')
plt.plot(x, y2, color='#A6AAAB', marker='o')
plt.legend(y2, loc='lower right', fontsize=7, shadow=True, framealpha=1, facecolor='#66DDAA', edgecolor='#057FDD', title='Легенда')

ax = plt.subplot(3, 3, 4)
ax.set_xticks([2018, 2020, 2022])
ax.set_xticklabels(['2018 год', '2020 год', '2022 год'])
ax.set_yticks([106, 110, 118])
ax.set_yticklabels(['106%', '110%', '118%'])
plt.plot(x, y2, color='#0060FA', linestyle='-.', marker='v')
plt.legend(y2, loc='upper center', fontsize=8, shadow=True, framealpha=1, facecolor='#FFDB00', edgecolor='red', title="I\'m legend")
plt.xlabel('"Великолепная ось X"', fontsize=8, fontweight="regular", color='orange')
plt.ylabel('"Потрясающая ось Y"', fontsize=8, fontweight="regular", color='green')

ax = plt.subplot(3, 2, 4)
ax.set_xticks([2018, 2019, 2020, 2021, 2022])
ax.set_xticklabels(['2018 год', '2019 год', '2020 год', '2021 год', '2022 год'], color='#0048BA')
ax.set_yticks([102, 110, 114, 118])
ax.set_yticklabels(['102%', '110%', '114%', '118%'], color='#00826F')
plt.plot(x, y1, color='#009B84', marker='s')
plt.subplots_adjust(hspace=0.5)
plt.legend(y1, loc='lower right', fontsize=6, shadow=True, framealpha=1, facecolor='#A9D300', edgecolor='red', title="I\'m legend")
plt.xlabel('"Ось X"', fontsize=8, fontweight="bold")
plt.ylabel('"Ось Y"', fontsize=8, fontweight="bold")

plt.show()
plt.savefig('графикДЗ.png')
plt.close('all')
