"""
3: Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
"""

my_list = [2, 2, 5, 6, 12, 17, 17, 12]
new_list = []
for number in my_list:
    if my_list.count(number) == 1:
        new_list.append(number)

print(new_list)
