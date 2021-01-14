"""
Усложняем программу, добавил количество попыток :-)
Также добавил конструкцию try exception если пользователь введет не число
Добавил выбор уровня сложности
Добавил выбоор игроков
"""
import random
number = random.randint(1, 100)
user_answer = None
levels = {1: 10, 2: 7, 3: 5}
level = int(input('Уровни сложности: \n1 - 10 попыток\n2 - 7 попыток\n3 - 5 попыток\n'
                  'выберите уровень сложности: '))
count = 0
max_count = levels[level]

user_count = int(input('Введите количество игроков: '))
users = []
for user in range(user_count):
    user_name = input(f'Введите имя игрока {user+1}: ') #использовал {user+1} для отображения игрок 1 а не 0
    users.append(user_name)
print(users)


while user_answer != number:
    try:
        user_answer = int(input('Угадайте число:\n '))
    except ValueError:
        print('Нужно ввести число')
        continue
    count += 1
    left_count = (max_count - count)

    if count == max_count:
        print(f'Попытки закончились. Вы проиграли. Правильное число {number}')
        break

    elif user_answer > number:
        print('Слишком большое число\n')

    elif user_answer < number:
        print('Слишком маленькое число\n')

    print(f'Осталось попыток : {left_count}\n')
else:
    print('Поздравляю, вы угадали')