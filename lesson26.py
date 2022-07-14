###################################################################################
# - - - - - Манипуляции над данными с использованием библиотеки Pandas - - - - - #

import pandas as pd

df1 = pd.read_csv('df1.csv', sep='\t')
df2 = pd.read_csv('df2.csv', sep='\t')

print(df1.info())
print(df2.info())

print(df1.head())
print(df2.head())

print(df1.columns)
print(df2.columns)

print(df1.describe())  # describe Выводит среднее значение
print(df2.describe())  # describe Выводит среднее значение

print(df1['Grocery Item'].value_counts())  # value_counts добавляет доп. столбец и считает уникальные значения, нужно указывать колонку
print(df2['Recipe'].value_counts())  # value_counts добавляет доп. столбец и считает уникальные значения, нужно указывать колонку

print(df1['Grocery Item'].unique())  # unique выводит уникальные значения
print(df2['Recipe'].unique())  # unique выводит уникальные значения


###################################################################################
# Работа с несколькими файлами
# Часто одни и те же данные разделены на несколько файлов.
# Допустим, у нас есть масса файлов, следующих по структуре имен файлов: file1.csv,
# file2.csv, file3.csv и т. Д. Сила pandas в основном заключается в возможности
# манипулировать большими объемами структурированных данных, поэтому мы хотим
# иметь возможность собрать всю необходимую информацию в одну таблицу, чтобы мы
# могли анализировать совокупные данные

# Задание
# 1. У нас есть 5 разных файлов по 4 студентов в каждом. Эти файлы соответствуют
# структуре именования:
# stud0.csv
# stud1.csv
# До stud 4.csv
# Мы собираемся импортировать каждый файл с помощью pandas и объединить все записи
# в один DataFrame.
# Сначала создайте переменную с именем student_files и установите ее равной glob () всех
# файлов csv, которые мы хотим импортировать.
# 2. Создайте пустой список с именем df_list, в котором будут храниться все фреймы
# данных, которые мы создаем из файлов stud0.csv по stud5.csv.
# 3. Прокрутите имена файлов в student_files и создайте DataFrame из каждого файла.
# Добавьте этот DataFrame в df_list.
# 4. Объедините все фреймы данных в df_list в один фрейм данных, называемый
# студентами.
# 5. Выведите в консоль students и его размер.

import pandas as pd
import glob

student_files = glob.glob("stud*.csv")
df_list = []
for filename in student_files:
    data = pd.read_csv(filename, sep='\t')
    df_list.append(data)

# print(df_list)
students = pd.concat(df_list)  # concat склеивает всех dataFrame склеивает в один список, должно быть одинаковое кол-во столбцов
# students.to_csv('stud2.csv')  # Можем записать в новый файл
print(students)
print(len(students))

###################################################################################
# Работа с дубликатами
# Часто мы видим дублирующиеся строки данных во фреймах данных, с которыми мы
# работаем. Это может произойти из-за ошибок при сборе данных или при сохранении и
# загрузке данных

import pandas as pd

df = pd.read_csv('stud_cl.csv', sep='\t')
# pd.set_option('display.max_rows', None)
df.drop(['Unnamed: 0'], inplace=True, axis=1)

# df2 = df.duplicated()
# print(df2.sort_values())  # Показывает True по дубликатам


# print(df.duplicated())
print(df.duplicated().sum())  # Показывает кол-во дубликатов в файле
df.drop_duplicates(inplace=True)  # Удаляет дублирующие строки
df.reset_index(inplace=True, drop=True)  # После удаления делаем reset по index, т.е. обновляем индексы т.к. удалили дубликаты
print(df.duplicated().sum())
