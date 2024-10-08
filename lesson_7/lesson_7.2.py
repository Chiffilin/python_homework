# На вхід функції correct_sentence передається два речення.
# Необхідно повернути їх виправлену копію так, щоб вони завжди починалися з великої літери та закінчувалися крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою,
# додавати ще одну не потрібно, це буде помилкою


##### ver_1 #####
# def correct_sentence(text):
#     text = text[0].upper() + text[1:]
#     if not text.endswith('.'):
#         text += '.'
#     return text

#### ver_2 ####
def correct_sentence(text):
    sentences = text.split('. ')

    corrected_sentences = [sentence.capitalize() for sentence in sentences]
    result = '. '.join(corrected_sentences)

    if not result.endswith('.'):
        result += '.'

    return result

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
