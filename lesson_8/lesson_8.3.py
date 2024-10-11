

#### ver_1 ####
# def find_unique_value(some_list):
#    result = None
#    for number in some_list:
#        if some_list.count(number) == 1:
#            result = number
#    return result

#### ver_1.1 #####
# def find_unique_value(some_list):
#     result = None
#     uniq_set = set(some_list).difference()
#     for number in uniq_set:
#         if some_list.count(number) == 1:
#             result = number
#     return result

#### ver_2 ####
def find_unique_value(some_list):
    count_dict = {}
    # Підрахунок кількості входжень
    for number in some_list:
        count_dict[number] = count_dict.get(number, 0) + 1
    print(count_dict)
    # Пошук числа з 1 входженням
    for number in some_list:
        if count_dict[number] == 1:
            return number

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
