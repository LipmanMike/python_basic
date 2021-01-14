"""
Усложняем программу, добавил количество попыток :-)
Также добавил конструкцию try exception если пользователь введет не число
Добавил выбор уровня сложности
"""
import random
number = random.randint(1, 100)
user_answer = None
levels = {1: 10, 2: 7, 3: 5}
level = input('Уровни сложности: \n1 - 10 попыток\n2 - 7 попыток\n3 - 5 попыток\n'
                          'выберите уровень сложности: ')
if level.isdigit():
    count = 0
    max_count = levels[level]
    while user_answer != number:
        try:
            user_answer = int(input('Угадайте число: '))
        except ValueError:
            print('Нужно ввести число')
            continue
        count += 1
        left_count = (max_count - count)

        if count == max_count:
            print(f'Попытки закончились. Вы проиграли. Правильное число {number}')
            break

        elif user_answer > number:
            print('Слишком большое число')

        elif user_answer < number:
            print('Слишком маленькое число')

        print(f'Осталось попыток : {left_count}')
    else:
        print('Поздравляю, вы угадали')
else:
    print('Нужно ввести число')