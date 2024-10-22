#Написати програму, яка переміщає всі нулі у кінець списку.
#Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
#Порядок ненульових чисел має зберегтися!


# move_zeroes = [2, 0, 4, 6, 0, 7]
# move_zeroes.remove(0)
# print(move_zeroes)
# print(move_zeroes[3])
# move_zeroes.insert(6, move_zeroes[3])
# print(move_zeroes)
# del move_zeroes[3]
# print(move_zeroes)
# move_zeroes.append(0)
# print(move_zeroes)

#Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.
# Не забудьте, що перший елемент масиву має індекс 0.
# lля порожнього масиву результат завжди 0.
# #v1.
# sum_num =[3, 5, 7, 11]
# last_num = 0
# if len(sum_num) == 0:
#     print("Error: empty list")
# else:
#     last_num = sum_num[-1]
# print(last_num)
#
# for el in range(0,len(sum_num), 2):
#  print(sum_num[el])
# sum_num = sum(sum_num[0:len(sum_num):2])
# result = sum_num * last_num
# print("Result:", result)

##v2
# sum_num = [2, 4, 6, 8, 10]
#
# if len(sum_num) == 0:
#     print("Error: Empty list")
# else:
#     last_num = sum_num[-1]
#     even_sum = sum(sum_num[0:len(sum_num):2])
#     result = even_sum * last_num
#     print("Result:", result)






#Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім
# і другим з кінця.

# import random
#
# FIRST_LIST = 7
# num = []
# for i in range(FIRST_LIST):
#     num.append(random.randint(3, 10))
# print(num)
# new_list1 = num[0]
# print(new_list1)
# new_list2 = num[2]
# print(new_list2)
# new_list3 = num[-2]
# print(new_list3)
# result = [new_list1, new_list2, new_list3]
# print(result)








