
# ##ДЗ 7.1. Вітання
# def say_hi(name, age):
#     return f"Hi, I'm {name} and I'm {age} years old."
# # print(say_hi(name="", age=""))
# presents = input("Say you name: ")
# presents_1 = input("Say age:")
# print(say_hi(name=presents, age=presents_1))
# assert say_hi("Iryna", 26)== "Hi, I'm Iryna and I'm 26 years old."
# print(say_hi("Iryna", 26))
#
# print("OK")

#ДЗ 7.2. Модифікувати рядок
# def correct_sentence(text):
#     if not text:
#         return ""
#     corrected_text = text[0].upper() + text[1:]
#     if not corrected_text.endswith("."):
#         corrected_text += "."
#     return corrected_text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')

#Дз 7.3 Пошук підрядка

# def second_index(text, some_str):
#   first_index = text.find(some_str)
#   if first_index == -1:
#         return -1
#   second1_index = text.find(some_str, first_index + 1)
#   if second1_index == -1:
#       return None
#   return second1_index
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

# homework 7.4



# def common_elements():
#
#     list3 = {x for x in range(0,100,3)}
#     print(list3)
#     list5 = {i for i in range(0,100,5)}
#     print(list5)
#     common_list = list3.intersection(list5)
#     print(common_list)
#     return common_list
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('OK')


































