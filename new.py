###################################################################################
# lesson29 (Последнее)
# Нарисовать диаграммы для этого задания

# Решение Ильи
# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_csv ('Пациенты_new.csv', delimiter = ';', encoding = 'cp1251')
#
# print(df)
# print()
#
# print(df.info())
# print()
#
# print(df.duplicated().sum())
# print()
#
# df = df.drop_duplicates()
# # print(df.duplicated(subset='card_num').value_counts())
# df.dropna(subset=['gender', 'birth'], inplace=True)
# print(df.info())
# print()
#
# print(df.gender.unique())
#
# df['birth'] = pd.to_datetime(df.birth, dayfirst=True )
# df['last_visit'] = pd.to_datetime(df.last_visit, dayfirst=True )
#
# df['age'] = (pd.Timestamp('now') - df.birth).astype('m8[Y]')
# df = df[df.age<100]
# df = df[df.sales_cost<1000000]
#
# print(df.head())
# print()
#
# plt.subplot(2,1,1)
# plt.hist(df.age, bins=10)
# plt.title('Гистограмма возрастов')
# plt.xlabel('Возраст пациентов клиники')
# plt.ylabel('Количество пациентов')
# plt.legend('Возраст')
# # plt.show()
#
# plt.subplot(2,1,2)
# plt.hist(df.gender, bins=10)
# plt.title('Гистограмма половой принадлежности')
# plt.ylabel('Количество пациентов')
# plt.subplots_adjust(hspace=0.9, left=0, top=1)
# plt.savefig('Гистограмма возрастов и половой принадлежности.jpeg')
# plt.show()
#
#
# df_young = df[df.age<18]
# df_adult = df[df.age>=18]
#
# plt.subplot(2,1,1)
# plt.scatter(df_young.age, df_young.sales_cost)
# plt.title('Диаграмма рассеивания оплаченных сумм пациентов младшего возраста')
# plt.xlabel('Возраст пациентов')
# plt.ylabel('Оплаченные суммы')
# # plt.show()
#
# plt.subplot(2,1,2)
# plt.scatter(df_adult.age, df_adult.sales_cost)
# plt.title('Диаграмма рассеивания оплаченных сумм пациентов старшего возраста')
# plt.xlabel('Возраст пациентов')
# plt.ylabel('Оплаченные суммы')
# plt.subplots_adjust(hspace=0.9, left=0, top=1)
# # plt.figure(figsize=(12,12))
# plt.savefig('Диаграмма рассеивания.jpeg')
# plt.show()
#
# plt.subplot(2,1,1)
# plt.hist(df_young.age, bins=10)
# plt.title('Гистограмма пациентов младшего возраста')
# plt.xlabel('Возраст пациентов клиники')
# plt.ylabel('Количество пациентов')
# plt.legend('Возраст')
