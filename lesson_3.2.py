# Ваша програма має перенести останній елемент списку з кінця на початок, тобто, останній елемент списку має стати першим.
# Послідовність інших елементів не має змінюватися.
# Порожній список або список з одним елементом повинен залишитися незмінним.
# Кількість елементів у списку може бути будь-яким – нуль та більше!


# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10

list_1 = [12, 3, 4, 10]
# list_1 = [1]
#list_1 = []
# list_1 = [12, 3, 4, 10, 8]

# ver_1
print(list_1)
if list_1:
    temp = list_1.pop()
    list_1.insert(0,temp)
print(list_1)
