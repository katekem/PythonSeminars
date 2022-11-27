# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет
# n1 = int(input('Введите первое число: '))
# n2 = int(input('Введите первое число: '))
# if n1 == (n2**2) or n2 == (n1**2):
#     print('Да')
# else:
#     print('Нет')

# 2. Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
# a1 = int(input('Введите число 1: '))
# a2 = int(input('Введите число 2: '))
# a3 = int(input('Введите число 3: '))
# a4 = int(input('Введите число 4: '))
# a5 = int(input('Введите число 5: '))
# numbers = input('Введите 5 чисел через пробел: ')
# numbers = numbers.split(' ')
# print(type(int_numbers))
# max = 0
# for i in numbers:
#     if numbers[i] > max:
#         max = numbers[i]
# print(f'max = {max}')

# num = []
# for i in range(5):
#     x = int(input('Enter number: '))
#     num.append(x)
# max_t = num[0]
# for i in num:
#     if i > max_t:
#         max_t = i
# print(f'max = {max_t}')

# 2. Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
num1 = float(input('Enter number: '))
if num1 == int(num1):
    print('No')
else:
    num2 = int(num1*10) % 10
    print(num2)
