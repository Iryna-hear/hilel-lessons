
##ДЗ 5.2. Модифікувати калькулятор

# PUT_CHOOSE = "Y"
# while True:
#     operation_1 = []
#
#     operation = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n Enter your choice: "))
#     match operation:
#              case 1:
#                        num1 = input("Enter first number: ")
#                        num2 = input("Enter second number: ")
#                        print( "Answer is:" + str(int(num1) + int(num2)))
#
#              case 2:
#                        num1 = input("Enter first number: ")
#                        num2 = input("Enter second number: ")
#                        print("Answer is:" + str(int(num1) - int(num2)))
#
#              case 3:
#                        num1 = input("Enter first number: ")
#                        num2 = input("Enter second number: ")
#                        print("Answer is:" + str(int(num1) * int(num2)))
#              case 4:
#                        num1 = input("Enter first number: ")
#                        num2 = input("Enter second number: ")
#                        if int(num2) != 0:
#                            print("Answer is:" + str(int(num1) / int(num2)))
#                        else:
#                            print("Cannot divide by zero")
#
#              case _:
#                        print("Enter a value between 1 and 4")
#     continue_operation = input(f"Do you want to continue?, {PUT_CHOOSE} for continue:")
#
#     if continue_operation != PUT_CHOOSE:
#         print("Exiting")
#         break

##ДЗ 5.3. hashtag
# import string
# my_hashtag = "Try change this - now!"
# sentence = my_hashtag.translate (str.maketrans('', '', string.punctuation)).split()
# sentence_capitalized = [ word.capitalize() for word in sentence]
# print(sentence_capitalized)
# hashtag = "#"  + ''.join(sentence_capitalized)
# print(hashtag)
# if len(hashtag) > 140:
#     hashtag = hashtag[:140]
#     print("Too long hashtag")



















