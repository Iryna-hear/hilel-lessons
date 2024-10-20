#Ваша програма має перенести останній елемент списку з кінця на початок, тобто,
# останній елемент списку має стати першим. Послідовність інших елементів не має змінюватися.


# at_list = [2, 20, "five", 5, 7, "ten" ]
# print(at_list)
# print(at_list[-1])
# at_list.insert(0, at_list[-1])
# print(at_list)
# del at_list[-1]
# print(at_list)
# at_list.insert(0, at_list[-1])
#
#  home work 3.3
#  Ваша програма повинна вміти розділяти один список на два та помістити їх
# у новий список. Тобто, в результаті повинен вийти список із 2-х списків.
list_change = [1, 4, 5, 6]
list_half = len(list_change)// 2
if len(list_change) % 2 == 0:
 half1 = list_change[:list_half]
 half2 = list_change[list_half:]
 print(half1)
 print(half2)
else:
 half1 = list_change[:list_half]
 half2 = list_change[list_half+1:]
result = [half1, half2]
print(result)