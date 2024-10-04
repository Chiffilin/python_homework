# HW 6.3. Добуток чисел
# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.


while True:
    user_input = input("Enter number:")
    if user_input.isdigit():
        break
    else:
        print("Good try! ^-^ Try again")

while int(user_input) > 9:
    result = 1
    for char in user_input:
        result *= int(char)
    user_input = str(result)

print(user_input)

# Test ver
# str_list = ["999", "1000",asd "423", "33", "25", "1",]
#
# for number in str_list:
#     while int(number) > 9:
#         result = 1
#         # print(number)
#         for char in number:
#             result *= int(char)
#         number = str(result)
#     print(number)
