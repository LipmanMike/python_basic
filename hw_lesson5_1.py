"""
Практическое задание
1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
"""

""" Вариант решения № 1
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)
new_list = my_list_1 - my_list_2
print(new_list)
"""

"""Вариант решения № 2 Неправильный"""
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for number in my_list_1: # Программа работает некорректно, так как удаляется только первый элемент из повторяющихся
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)

""" Вариант решения № 3 Правильный """
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for number in my_list_1[:]: # Создаем в цикле копию списка, из которого удаляем элементы
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)