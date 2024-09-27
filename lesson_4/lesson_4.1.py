# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!

list_1 = [0, 1, 0, 12, 3]
# list_1 = [0]
# list_1 = [1, 0, 13, 0, 0, 0, 5]
# list_1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


# ver_1
movement_number = 0 # потрібне число для пошуку
for number in list_1:
    temp = list_1.pop(list_1.index(movement_number))
    list_1.append(temp)
print(list_1)

# ver_2
# movement_number = 0 # потрібне число для пошуку
# count_number = list_1.count(0) # кількість потрібного числа
# list_len = len(list_1) # розмір ліста
# count_find = 0    # кількість знайдених чисел
# index = 0 # індекс числа ліста

# while count_find < count_number:
#     if list_1[index] == movement_number:
#         temp = list_1.pop(index)
#         list_1.insert(list_len,movement_number)
#         count_find += 1
#         index -=1
#     index += 1
# print(list_1)

