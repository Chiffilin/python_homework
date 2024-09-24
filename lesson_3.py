#HW 3.1. Найпростіший калькулятор
#Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма,
# виходячи з дії, обчислює та друкує результат.
#Зробити перевірку на те, що при діленні дільник не дорівнює 0!

first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
user_operator = input("Enter operation (+,-,*,/):")
answer = 0

if user_operator == "+" or "-" or "*" or '/':
    if user_operator == '+':
        answer = first_number + second_number
    elif user_operator == '-':
        answer = first_number - second_number
    elif user_operator == '*':
        answer = first_number * second_number
    elif user_operator == '/':
        if second_number == 0:
            print("You can't divide by zero")
        else:
            answer = first_number / second_number
    if second_number != 0:
        print(f"{first_number}{user_operator}{second_number}={answer}")
else:
    print("Incorrect operator entered!")
