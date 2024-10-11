#### ver_1 ####
# def add_one(some_list):
#     temp = ''
#     for number in some_list:
#         temp += str(number)
#     temp = str(int(temp) + 1)
#     result_list = []
#     for number in temp:
#         result_list.append(int(number))
#     return result_list

#### ver_2 #####
def add_one(some_list):
    number = int(''.join(map(str, some_list)))  # Список у число
    number += 1
    return list(map(int, str(number)))  # Число у список

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
