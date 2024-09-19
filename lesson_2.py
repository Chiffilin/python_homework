#HW 2.1. Виведення числа в стовпчик
#first ver
user_input = int(input("Enter your number:"))
user_input_v2 = user_input

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


