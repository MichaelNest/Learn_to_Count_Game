import random

low_diapason = 10
high_diapason = 100
sign = 0
play_game = True
count = 0
right = 0
score = 0

print('''Компьютер составляет пример. Введите ответ: 
Для завершения работы введите STOP''')
print('*'*43)

while(play_game):
    print(f'Ваши очки: {score}')
    print(f'Обработано задач: {count}')
    print(f'Правильных ответов: {right}')
    print('-'*43)

    sign = random.randint(0, 3)

    if (sign == 0): # Сложение
        z = random.randint(low_diapason, high_diapason)
        x = random.randint(low_diapason, z)
        y = z - x
        if(random.randint(0, 1) == 0):
            print(f'{x} + {y} = ?')
        else:
            print(f'{y} + {x} = ?')

    elif(sign == 1): # Вычитание
         x = random.randint(low_diapason, high_diapason)
         y = random.randint(0, x-low_diapason)
         z = x - y
         print(f'{x} - {y} = ?')

    elif(sign == 2): # умножение
        x = random.randint(1, (high_diapason-low_diapason) //
                           random.randint(1, high_diapason // 10)+1)
        y = random.randint(low_diapason, high_diapason) // x
        x = x * y

        print(f'{x} * {y} = ?')

    elif(sign == 3): # деление
        x = random.randint(1, (high_diapason - low_diapason)//
                           random.randint(1, high_diapason//10)+1)
        y = random.randint(low_diapason, high_diapason)//x
        if(y == 0):
            y = 1
        x = x * y
        z = x // y
        print(f'{x} / {y} = ?')

    user = ''
    while(not user.isdigit()
          and user.upper() != 'STOP'
          and user.upper() != 'S'
          and user.upper() != 'Ы'
          and user.upper() !='ЫЕЩЗ'):
        user = input('Ваш ответ?')

        if (user.upper() == 'HELP'
                or user == '?'
                or user == ','
                or user.upper() == 'РУДЗ'):
            if(z>9):
                print(f'Последняя цифра ответа: {z % 10}')
            else:
                print('Ответ состоит из одной цифры, подсказка невозможна!!')
            score -=10
        elif(user.upper() == 'STOP'
            or user.upper()=='S'
            or user.upper() == 'Ы'
            or user.upper() == 'ЫЕЩЗ'):
            play_game = False
        else:
            count+=1
            if(int(user) == z):
                print('\nПравильно!!\n')
                right +=1
                score +=10
            else:
                print((f'\nОтвет не правильный... Правильно: {z}'))
                print(f'Вы можете ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (-10 очков)\n')
                score -=20
print('*'*45)
print('СТАТИСТИКА ИГРЫ: ')
print(F'Всего примеров: {count}')
print(F'Правильных ответов: {right}')
print(F'Неправильных ответов: {count - right}')

if(count > 0):
    print(f'Процент верных ответов: {int(right/count * 100)}%')
else:
    print('Процент верных ответов: 0%')
print('Возвращайтесь!!')














