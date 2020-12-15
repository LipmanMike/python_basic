import random
number = random.randint(1, 101)

while True:
    user_answer = int(input('Угадайте число: '))
    if user_answer == number:
        print('Поздравляю, вы угадали')
        break
    elif user_answer > number:
        print('Слишком большое число')
    elif user_answer < number:
        print('Слишком маленькое число')




