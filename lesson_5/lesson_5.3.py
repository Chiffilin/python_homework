# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.

# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string
my_string = input("Введіть рядок для перетворення в hashtag: ")

# print(len(my_string))

new_string = my_string.title()
removed_characters = string.punctuation + " "
new_string = ''.join(char for char in new_string if char not in removed_characters)
result = "#{}".format(new_string)

if len(result) > 140:
    result = result[:140]

print(result)


############################################ Test ver #####################################################
# ласт стрінга довжиною у 150 символів

# my_string_list = ['Python Community','i like python community!','Should, I. subscribe? Yes!',
# '12345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512'
# '3451234512345123451234512345123451234512345123451234512345']
# for my_str in my_string_list:
#     my_str = my_str.title()
#     removed_characters = string.punctuation + " "
#     my_str = ''.join(char for char in my_str if char not in removed_characters)
#     result = "#{}".format(my_str)
#
#     if len(result) > 140:
#         result = result[:140]
#
#     print(result, f"Довжина:{len(result)}")