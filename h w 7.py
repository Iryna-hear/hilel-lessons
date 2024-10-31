
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
def correct_sentence(text):



assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

