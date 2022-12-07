import random
# my_list = [random.randint(0,100) for x in range(10) if x%2 == 0]
# # можно число вместо рандома
# print(my_list)



# def random_letter():
#     num = random.randint(0,100)
#     if num%2 == 0:
#         return '100'
#     else:
#         return '1'
# my_list = [random_letter() for x in range(10) if x%2 == 0]
# my_list = list(map(int, my_list))
# my_list = list(map(lambda x: x**2, my_list))
# print(my_list)

# my_list = list(filter(lambda x: x>90, my_list))
# print(my_list)


# def random_letter():
#     num = random.randint(0,100)
#     if num%2 == 0:
#         return 'A'
#     else:
#         return 'B'
# # my_list = [random_letter() for x in range(10)]
# print(my_list)

# for i, item in enumerate(my_list):
#     if item == 'B':
#         print(i, item)

# first_list = [random_letter() for x in range(10)]
# print(first_list)
# second_list = [random_letter() for x in range(10)]
# print(second_list)
# third_list = [random_letter() for x in range(10)]
# print(third_list)
# all_list = list(zip(first_list, second_list, third_list))
# print(all_list)

# def random_letter():
#     num = random.randint(0,100)
#     if num%2 == 0:
#         return 4
#     else:
#         return 5

# my_list = [random_letter() for x in range(10)]
# print(my_list)

# # В файле находится N натуральных чисел, записанных через пробел. 
# # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# # Найдите это число.
# path = r'/Users/ekaterinakemenova/Desktop/python/HelloPython/Seminars/result.txt'
# file = open(path, 'w', encoding='UTF-8')
# string = 'sdfg'
# file.write(string)
# file.close

# path = r'/Users/ekaterinakemenova/Desktop/python/HelloPython/Seminars/result.txt'
# string = 'sdfg'
# with open(path, 'w', encoding='UTF-8') as file:
#     file.write(string)

# with open(path, 'r', encoding='UTF-8') as file:   #можно букву вместо file
#     data = file.readline()
# print(data)

# with open('res.txt', 'r') as data:
#     string = data.readline()

# print(string)
# string = string.split()
# print(string)
# string = list(map(int, string))
# print(string)

# for i in range(1, len(string)):
#     if string[i]-1 != string[i-1]:
#         print(f'Потерянное число = {string[i-1]+1}')


## Дан список чисел. Создайте список, в который попадают числа,
## описываемые возрастающую последовательность.
## Порядок элементов менять нельзя.
my_list = [random.randint(0,10) for _ in range(10)]
print(my_list)

for i in range(len(my_list)):
    result = []
    max = my_list[i]
    result.append(my_list[i])
    for j in range(len(my_list)-1):
        if my_list[j] > max:
            result.append(my_list[j])
            max = my_list[j]
print(result)



