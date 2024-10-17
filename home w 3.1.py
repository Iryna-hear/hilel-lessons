operation = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\nEnter your choice: "))

if operation == 1:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print( "Answer is:" + str(int(num1) + int(num2)))
elif operation == 2:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("Answer is:" + str(int(num1) - int(num2)))
elif operation == 3:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("Answer is:" + str(int(num1) * int(num2)))
elif operation == 4:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("Answer is:" + str(int(num1) / int(num2)))
    if num1 or num2 == 0:
        print("Cannot divide by zero")

else:
    print(0)



