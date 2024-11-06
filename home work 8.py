#8.1 add 1 to number
# #v1
# def add_one(some_list):
#     list1 = []
#     first_sum = ""
#     for i in list1:
#         first_sum += str(i)
#     second_sum = int(first_sum) + 1
#     result = [int(i) for i in str(second_sum)]
#     return result
#
# print('All tests passed!')


#v2
# def add_one(some_list):
#      list1 = []
#      first_sum = "".join(map(str, list1))
#      print(first_sum)
#      second_sum = int(first_sum) + int(1)
#      print(second_sum)
#      result = list(map(int, str(second_sum)))
#      print(result)
#      return result
#
#
#
# print('All tests passed!')





#ДЗ 8.2. palindrome
#
# def is_palindrome(text):
#       unique_va = ""
#       correct_value = "".join(unique_va) and unique_va.lower() and unique_va.isalpha()
#       if  correct_value == correct_value[::-1]:
#             return True
#       else:
#             return False
#

# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print('All tests passed!')


# ДЗ 8.3. Унікальне число

# def find_unique_value(some_list):
#    unique_number = {}
#    for item in some_list:
#        unique_number[item] = unique_number.get(item, 0) + 1
#    for item, count in unique_number.items():
#        if count == 1:
#            return item
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")







