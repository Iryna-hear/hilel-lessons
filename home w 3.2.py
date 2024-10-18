#Ваша програма має перенести останній елемент списку з кінця на початок, тобто,
# останній елемент списку має стати першим. Послідовність інших елементів не має змінюватися.
at_list = [2, 20, "five", 5, 7, "ten" ]
print(at_list)
print(at_list[-1])
at_list.insert(0, at_list[-1])
print(at_list)
del at_list[-1]
print(at_list)
at_list.insert(0, at_list[-1])



