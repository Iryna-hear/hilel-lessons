#ДЗ 10.3. Перевірити чи є парним чи ні
# def is_even(digit):
#
#
# #v1
#  # return divmod(digit,2)[1]== 0
# #v2
#  return digit % 2 == 0
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')
from itertools import count


# #ДЗ 10.2. Знайти перше слово
# import re
# def first_word(text):
#     result = re.search(r"[a-zA-Z']+", text)
#     return result.group()
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')


#ДЗ 10.1. Генераторна функція
# def pow(x):
#     return x ** 2
#
# def some_gen(begin, end, func):
#     count = 0
#     while count < end:
#       yield begin
#       begin = func(begin)
#       count += 1
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')
