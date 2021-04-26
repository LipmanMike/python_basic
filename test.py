# user_numbers = []
# for i in range(3):
#     number = int(input('введите число: '))
#     user_numbers.append(number)
# print(max(user_numbers))
# print(min(user_numbers))
# print(sum(user_numbers))

# def search4letters(phrase: str, letters: str) -> set:
#     """Возвращает найденные буквы во фразе"""
#     return set(letters).intersection(set(phrase))
#
# search4letters('hello world', 'e')

def greeting(say, *args):
    print(say, *args)

greeting('Greeting', 'Mike', 'Kate', 'Leo')