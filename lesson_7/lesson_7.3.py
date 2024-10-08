from itertools import count


#### ver_1 ####
# def second_index(text, some_str):
#   if text.index(some_str) == text.rindex(some_str):
#       result = None
#   else:
#       result = text.rindex(some_str)
#   return result

#### ver_2 ####
def second_index(text, some_str):
    first_occurrence = text.find(some_str)
    result = None
    if first_occurrence != -1:
        second_occurrence = text.find(some_str,first_occurrence+1)
        if second_occurrence != -1:
            result = second_occurrence
    return result

#### ver_2.1 ####
# def second_index(text, some_str):
#     if text.find(some_str) < text.find(some_str,text.find(some_str)+1):
#         result = text.find(some_str,text.find(some_str)+1)
#     else:
#         result = None
#     return result


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
