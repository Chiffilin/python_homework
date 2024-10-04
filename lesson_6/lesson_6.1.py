import string

# v_1
usr_inpt = input("""Enter first and last letter "a-c": """)
print(f"{string.ascii_letters[string.ascii_letters.index(usr_inpt[0]):string.ascii_letters.index(usr_inpt[-1])+1]}")

# v_1.1
# usr_inpt = input("""Enter first and last letter "a-c": """)
# my_letters = (string.ascii_letters)
# print(my_letters[my_letters.index(usr_inpt[0]):my_letters.index(usr_inpt[-1])+1])