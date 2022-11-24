# numbers = input('Введите число: ')
# count = int(input('Введите точность: '))

# print(numbers[0:4])
# print(numbers)
# numbers = numbers.split('.')
# print(numbers)
# print(float(numbers[0] + '.' + numbers[1][0:count]))

# numbers = int(input('Введите размер списка: '))
# my_list = [i for i in range(numbers)]
# print(my_list)
# print(my_list[:-3])

# numbers = int(input('Введите размер списка: '))
# my_list = [i for i in range(numbers)]

# def digit_after_dot_counter(num:float):
#     count = 0
#     div = 1
#     while True:
#         if num*div != int(num*div):
#             count *=1
#             div *=10
#         else: break
#     return count

# print(digit_after_dot_counter(numbers))

# from decimal import Decimal
# numbers = float(input('Введите размер списка: '))
# number0 = (numbers*100)/10
# numberD = (Decimal(str(numbers))*100)/10
# print(number0)
# print(numberD)

# coords = input('Введите координаты через пробел: ')
# coords = coords.split(' ')
# print(coords)
# if len(coords)/2 == 2:
#     print('2D')
#     for item in coords:
#         print(int(item))
#         print(type(item))
# elif len(coords)/2 == 3:
#     print('3D')
# else:
#     print('Введены не корректные координаты')

# Задача 1. Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N
# *Примеры:* 
#5
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = int(input('Введите число: '))
# my_list = []

# for i in range(-number, number + 1):
#     my_list.append(i)

# print(my_list)

# for i in my_list:
#     print(i, end=', ')

# print(*my_list, sep = ', ')

# Задача 2. Напишите программу, которая принимает на вход число 
# и проверяет, кратно ли оно 5 и 10 или 15, но не 30

# number = int(input('Введите число: '))
# if (number%10 == 0 or number%15 == 0) and number %30 != 0:
#     print('Условие выполнено')
# else:
#     print('Условие не выполнено')

# Задача: Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
# *Пример:*  
# - Для N = 5: 1, -3, 9, -27, 81

# my_list = []
# N = int(input('Введите число:'))
# for i in range(N):
#     my_list.append((-3)**i)
# print(*my_list, sep = ', ')

# for i in range(number-1):      # другой вариант решения
#     my_list.append(my_list[i]*(-3))

# Задача: Для натурального n создать список,
# состоящий из элементов последовательности 3*n + 1.
# *Пример:*
# - Для n = 6: ['1: 4', '2: 7', '3: 10', '4: 13', '5: 16', '6: 19']
# N = int(input('Введите число:'))
# my_list = [0] * N
# for i in range(N):
#     my_list[i] = f'{i+1}: {3*(i+1) + 1}'
# print(my_list)

# Задача: Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
# со строками через срезы
