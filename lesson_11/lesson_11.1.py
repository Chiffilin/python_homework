#### ver_1 ####
# def is_prime(n: int) -> bool:
#     """Перевіряє, чи є число простим."""
#     if n <= 1:
#         return False
#     # Перевіряємо подільність тільки до кореня числа
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def prime_generator(end):
#     number = 0
#     while number <= end:
#         if is_prime(number):
#             yield number
#         number += 1

#### ver_2 ####
def is_prime(n: int) -> bool:
    """Перевіряє, чи є число простим."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Перевіряємо подільність тільки для чисел виду 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(end):
    number = 2
    while number <= end:
        if is_prime(number):
            yield number
        number += 1


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
