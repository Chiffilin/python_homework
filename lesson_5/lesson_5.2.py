loop_work = True
while loop_work:
    first_number = float(input("Enter first number:"))
    second_number = float(input("Enter second number:"))
    user_operator = input("Enter operation (+,-,*,/):")
    answer = 0

    if user_operator in ("+", "-", "*", "/"):
        if user_operator == '+':
            answer = first_number + second_number
        elif user_operator == '-':
            answer = first_number - second_number
        elif user_operator == '*':
            answer = first_number * second_number
        elif user_operator == '/':
            if second_number != 0:
                answer = first_number / second_number
            else:
                print("You can't divide by zero")
        if second_number != 0:
            print(f"{first_number}{user_operator}{second_number}={answer}")
    else:
        print("Incorrect operator entered!")

    user_answer = input("Enter (y) or (yes) to continue:")
    if user_answer in ("y","yes"):
        loop_work = True
    else:
        loop_work = False
        print("See you later!")
