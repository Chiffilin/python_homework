# HW 6.2. Конвертер із числа в дату

user_input = int(input("Enter second's:"))

if 0 <= user_input < 8640000:
    day, hour = divmod(user_input,24*60*60)
    hour, minutes = divmod(hour,60*60)
    minutes, seconds = divmod(minutes,60)
    my_str = "дні"
    if day % 2 or day == 0:
        my_str = "днів"
    print(f"{day} {my_str}, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print("Error: out of range ( 0 <= input < 8640000")


# test_numbers = [0, 224930, 466289, 950400, 1209600, 1900800, 8639999, 22493, 7948799]
# for number in test_numbers:
#     if 0 <= number < 8640000:
#         day, hour = divmod(number, 24 * 60 * 60)
#         hour, minutes = divmod(hour, 60 * 60)
#         minutes, seconds = divmod(minutes, 60)
#         my_str = "дні"
#         if day % 2 or day == 0:
#             my_str = "днів"
#         print(f"{day} {my_str}, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
#     else:
#         print("Error: out of range ( 0 <= input < 8640000")
