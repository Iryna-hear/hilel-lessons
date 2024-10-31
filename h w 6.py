# ##ДЗ 6.2. Конвертер із числа в дату
# MIN_TIME = 0
# MAX_TIME = 8640000
# DAY = (24 * 60 * 60)
# HOUR = (60 * 60)
# MINUTE = 60
# clock = int(input("Enter seconds:"))
# if clock <= MIN_TIME or clock > MAX_TIME:
#     print(f"Number within {MIN_TIME} and {MAX_TIME} ")
#     exit()
# days = clock // DAY
# if days >= 0:
#  print(days,"Days", end= " " )
# hours = (clock % DAY) // HOUR
# print(str(hours).zfill(2), end=  ":")
# minutes = (clock % HOUR) // MINUTE
# print(str(minutes).zfill(2), end= ":")
# seconds = clock % MINUTE
# print(str(seconds).zfill(2), end= " ")


##ДЗ 6.1. Діапазон букв
# import string
# from string import ascii_letters
# letters = string.ascii_letters
# print(letters)
# user_e = input("Enter your letters: ")
#
# first_l, last_l = user_e.split("-")
# first_index = string.ascii_letters.index(first_l)
# second_index = string.ascii_letters.index(last_l)
# result = string.ascii_letters[first_index:
#          second_index+1]
# print("Result: ", result )

#ДЗ 6.3. Добуток чисел

#
