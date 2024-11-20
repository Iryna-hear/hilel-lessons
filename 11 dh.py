#ДЗ 11.3. Перевірка на парність.

# def is_even(number):
 # v1
#       last_number = str(number)[-1]
#       return last_number in "02468"


# v2
      # while number > 0:
      #   number -= 2
      # return  number == 0


# print("All tests passed")
# assert is_even(2494563894038 ** 2) == True, 'Test1'
# assert is_even(1056897 ** 2) == False, 'Test2'
# assert is_even(24945638940387 ** 3) == False, 'Test3'

#ДЗ 11.1. Генератор простих чисел

# def prime_generator(end):
#         if end  >= 2:
#             yield 2
#         for num in range(3, end + 1, 2):
#             find_prime = True
#             for i in range(3, int(num ** 0.5) + 1, 2):
#                 if num % i == 0:
#                     find_prime = False
#                     break
#             if find_prime:
#                 yield num
#
# from inspect import isgenerator
#
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')

#ДЗ 11.2. Заповнення списку кубами чисел

# def generate_cube_numbers(end):
#     numbers = 2
#     while True:
#         result = numbers ** 3
#         if result > end:
#             return
#         yield result
#         numbers += 1
#
#
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8]
# assert list(generate_cube_numbers(100)) == [8, 27, 64]
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]





