# Змінна не може:
# -починатися з цифри !
# -містити великі літери,
# -пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# -бути жодним із зареєстрованих слів.
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

user_input = input("Введіть назву змінної: ")

# Пунктуацію без символу підкреслення
punctuation_without_underscore = string.punctuation.replace('_', '')

# 1. Перевірка, чи починається рядок з цифри
if user_input[0].isdigit():
    result = False
# 2. Перевірка на наявність великих літер
elif any(char.isupper() for char in user_input):
    result = False
# 3. Перевірка на ключові слова
elif user_input in keyword.kwlist:
    result = False
# 4. Перевірка на пробіли та недопустимі символи
elif any(char in punctuation_without_underscore for char in user_input) or any(char.isspace() for char in user_input):
    result = False
# 5. Перевірка, щоб рядок не складався більше ніж 1 підкреслення
elif user_input.strip("_") == "" and user_input.count("_") > 1:
    result = False
else:
    result = True

print(result)

# if result:
#     print("Змінна створена!")
# else:
#     print("Порушені правила створення змінних!")

############################# auto_test_ver ###################################

# my_list = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value",
#            "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]
#
# # Пунктуацію без символу підкреслення
# punctuation_without_underscore = string.punctuation.replace('_', '')
#
# result = True
#
# for my_string in my_list:
#     # 1. Перевірка, чи починається рядок з цифри
#     if my_string[0].isdigit():
#         result = False
#     # 2. Перевірка на наявність великих літер
#     elif any(char.isupper() for char in my_string):
#         result = False
#     # 3. Перевірка на ключові слова
#     elif my_string in keyword.kwlist:
#         result = False
#     # 4. Перевірка на пробіли та недопустимі символи
#     elif any(char in punctuation_without_underscore for char in my_string) or any(char.isspace() for char in my_string):
#         result = False
#     # 5. Перевірка, щоб рядок не складався більше ніж 1 підкреслення
#     elif my_string.strip("_") == "" and my_string.count("_") > 1:
#         result = False
#     else:
#         result = True
#     print(my_string,result)