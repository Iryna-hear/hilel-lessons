# ввести 4-х значне число з клавіатури, після чого друкує на екрані стовпчик цифр, з якого це число складається.
number = 5649
number1 = number // 1000
number2 = number % 1000 // 100
number3 = number % 100 // 10
number4 = number % 10

print(number1)
print(number2)
print(number3)
print(number4)

result = number1 + number2 + number3 + number4
print("Result :" , result)



