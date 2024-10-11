#### ver_1 ####
# def is_palindrome(text):
#     temp =  ''.join(filter(str.isalpha and str.isalnum, text)).lower()
#     return temp == temp[::-1]

#### ver_2 ####
import re
def is_palindrome(text):
    cleaned_str = re.sub(r'[^a-zA-Z0-9]','',text.lower())
    return cleaned_str == cleaned_str[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
