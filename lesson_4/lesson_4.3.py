# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця

import random
# оптимальний варіант рішення
my_list = [random.randint(1,10) for i in range(random.randint(3, 10))]
#my_list = [1, 2, 3, 4, 5, 6, 7, 9]
# my_list = [1, 1, 2, 1]
# my_list = [6, 3, 7]

indices = [0, 2, -2]
new_list = []

# ver_1
for index in indices:
    new_list.append(my_list[index])
print(my_list,new_list, sep= " == ")

# ver_2
new_list_2 = [my_list[index] for index in indices]
print(f'{my_list} == {new_list_2}')