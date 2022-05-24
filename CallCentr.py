# Задача колл-центр
mn1 = False
mn2 = False
mn3 = False
gen_mn = 'Главный менеджер'
human = 1

if ((mn1 == True) and (mn2 == True) and (mn3 == True)) | ((mn1 == True) and (mn2 == False) and (mn3 == False)):
    print('Ваш менеджер mn1')
elif ((mn1 == False) and (mn2 == True) and (mn3 == True)) | ((mn1 == False) and (mn2 == True) and (mn3 == False)):
    print('Ваш менеджер mn2')
elif ((mn1 == True) and (mn2 == False) and (mn3 == True)) | ((mn1 == False) and (mn2 == False) and (mn3 == True)):
    print('Ваш менеджер mn3')
elif (mn1 == False) and (mn2 == False) and (mn3 == False) and (human < 2):
    print('Ожидание оператора')
elif (mn1 == False) and (mn2 == False) and (mn3 == False) and (human >= 2):
    print('Ваш менеджер gen_mn')



