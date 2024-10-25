#### ver_1 ####
# def generate_cube_numbers(end):
#     number = 2
#     while number < end:
#         cube_num = number ** 3
#         if cube_num <= end:
#             yield cube_num
#         number += 1


#### ver_2 ####
def generate_cube_numbers(end):
    number = 2  
    while (cube_num := number ** 3) <= end:
        yield cube_num
        number += 1


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('Ok')
