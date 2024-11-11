# #ДЗ 9.1. Визначити популярність певних слів у тексті
#
# def popular_words(text, words):
#     pop_words = {}
#     text = text.lower().split()
#     for word in words:
#         pop_words[word] = text.count(word)
#     return pop_words
#
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')
from sys import prefix


# #ДЗ 9.2. Різниця між числами
# def difference (*numbers):
#     if len(numbers) == 0:
#         return 0
#     max_number = max(numbers)
#     min_number = min(numbers)
#     difference_between_num = max_number - min_number
#
#     return round(difference_between_num, 1)
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')

