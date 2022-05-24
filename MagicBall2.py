import random # Импортируем модуль random
name = ''
while len(name.strip()) < 1:
    print("Привет! Давай знакомиться! Как тебя зовут?")
    name = input()
question = ''
while len(question.strip()) < 1:
    print(name + "!" + " Можешь задать вопрос магическому шару")
    question = input()
random_num = random.randint(1, 9)

if random_num == 1:
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
Магический шар отвечает: %s''' % (name, question, answer))