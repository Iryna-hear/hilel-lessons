# необхідно перевернути 5-ти значне число


#number_full = int(input("Enter a number: ")) # 78965
number = 78965
n1 = number // 10000
n2 = number % 10000 // 1000
n3 = number % 1000 // 100
n4 = number % 100 // 10
n5 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print("Result: ", result)




