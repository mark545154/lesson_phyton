import random # Импортируем модуль random
name = input('Введите Ваше имя: ')
question = input('Введите вопрос: ')
random_num = random.randint(1, 9)

if not name:
    print('Представьтесь пожалуйста:)')
    if not question:
        print('Введите Ваш вопрос')
elif random_num == 1:
    answer = 'Да, безусловно.'
elif random_num == 2:
    answer = 'Это решительно так.'
elif random_num == 3:
    answer = 'Без сомнения.'
elif random_num == 4:
    answer = 'Ответ туманный, попробуйте еще раз.'
elif random_num == 5:
    answer = 'Спросите еще раз позже.'
elif random_num == 6:
    answer = 'Лучше не говорить вам сейчас.'
elif random_num == 7:
    answer = 'Мои источники говорят «нет».'
elif random_num == 8:
    answer = 'Прогноз не очень хороший.'
elif random_num == 9:
    answer = 'Очень сомнительно.'
else:
    answer = 'Попробуйте зайти позже'

print('''%s спрашивает: %s
Магический шар отвечает: %s'''%(name, question, answer))

# print(name, 'спрашивает: ', question)
# print('Магический шар отвечает: ', answer)