
# Дешиврування методу
crypt_result = "хѶѭѳQѲѴѫѬѳѬѿѱѱRod"
my_key = "432513"

decrypt_result = ""
for index,char in enumerate(crypt_result):
    key_index = index % len(my_key)
    decrypt_result += (chr(ord(char) - ord(my_key[key_index])))
print(decrypt_result)



#Метод шифрування Виженера
# my_string = ("Що потрібно шифрувати")
# my_key = "432513"
# crypt_result = ""
#
# for index, char in enumerate(my_string):
#     key_index = index % len(my_key)
#     crypt_result += (chr(ord(char) + ord(my_key[key_index])))
# print(crypt_result)