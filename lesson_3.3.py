# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

list_1 = [1, 2, 3, 4, 5, 6]
# list_1 = [1, 2, 3]
# list_1 = [1, 2, 3, 4, 5]
# list_1 = [1]
# list_1 = []


# ver_1
list_2 = []
size_list = len(list_1)
half_size = int(size_list / 2)
if not size_list % 2:
    list_2 = [list_1[:half_size], list_1[half_size:]]
else:
    half_size += 1
    list_2 = [list_1[:half_size],list_1[half_size:]]
print(list_2)