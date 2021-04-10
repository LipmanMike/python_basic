"""
Усложняем программу, добавил количество попыток :-)
"""
import random
number = random.randint(1, 100)
user_answer = None
count = 0
max_count = 7

while user_answer != number:
    user_answer = int(input('Угадайте число: '))
    count += 1
    left_count = (max_count - count)

    if count > max_count:
        print(f'Попытки закончились. Вы проиграли. Правильное число {number}')
        break

    elif user_answer > number:
        print('Слишком большое число')

    elif user_answer < number:
        print('Слишком маленькое число')

    print(f'Осталось попыток : {left_count}')
else:
    print('Поздравляю, вы угадали')