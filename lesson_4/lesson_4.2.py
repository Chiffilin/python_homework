# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.
# Не забудьте, що перший елемент масиву має індекс 0.
# Для порожнього масиву результат завжди 0.

# list_1 = [0, 1, 7, 2, 4, 8]
list_1 = [1, 3, 5]
# list_1 = [6]
# list_1 = []

answer_sum_and_multiplication = 0
for number_on_index in list_1:
    if not list_1.index(number_on_index) % 2:
        answer_sum_and_multiplication += number_on_index
else:
    if list_1:
        answer_sum_and_multiplication *= list_1[-1]
print(f'{list_1} => {answer_sum_and_multiplication}')