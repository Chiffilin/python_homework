#HW 2.1. Виведення числа в стовпчик
user_input = int(input("Enter your number:"))
user_input_v2 = user_input

print("#HW 2.1. Виведення числа в стовпчик")

#first ver
print(user_input // 1000)
user_input %= 1000
print(user_input // 100)
user_input %= 100
print(user_input // 10)
user_input %= 10
print(user_input)

#second ver
print(divmod(user_input_v2,1000))
print(divmod(user_input_v2%1000,100))
print(divmod(user_input_v2%100,10))
print(divmod(user_input_v2%10,1))


# #HW 2.2. Необхідно "перевернути" 5-ти значне число
user_input = int(input("Enter your number:"))
user_input_v2 = user_input

print(""""#HW 2.2. Необхідно "перевернути" 5-ти значне число""")

#first ver
number_1 = user_input % 10
number_2 = (user_input // 10) % 10
number_3 = (user_input // 100) % 10
number_4 = (user_input // 1000) % 10
number_5 = (user_input // 10000) % 10

print(f'{number_1}{number_2}{number_3}{number_4}{number_5}')

# second ver
print(user_input % 10)
user_input //= 10
print(user_input % 10)
user_input //= 10
print(user_input % 10)
user_input //= 10
print(user_input % 10)
user_input //= 10
print(user_input % 10)

# second ver
print(divmod(user_input_v2 % 10,1))
print(divmod(user_input_v2 % 100,10))
print(divmod(user_input_v2 % 1000,100))
print(divmod(user_input_v2 % 10000,1000))
print(divmod(user_input_v2 % 100000,10000))