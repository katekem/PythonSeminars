my_list = [1, 2, 3, 4, 5, 6]             # список
my_tuple = (1, 2, 3, 4, 5, 6)            # кортеж
my_set = {1, 2, 3, 4, 5, 6}              # множество
my_dict = {1:'one', 2:'two', 3:'three'}  # словарь

my_list.append()
my_list.pop()  # по индексу
my_list.remove()  # по значению (убирает первое вхождение)
pop_elem = my_list.pop(2)
print(pop_elem)
my_list.append(pop_elem)
my_list.insert(0,pop_elem)  # можно поставить куда угодно, 
                            # вначале указать позицию
print(my_list.count(2))     # значение в скобках - сколько раз встречается
my_list2 = [7, 8, 9]
my_list.extend(my_list2)
my_list.reverse()
my_list.index(2)   # указывает индекс элемента
my_list[0:3]  # без изменения
my_list = my_list[0:3]
my_list = my_list[::-1]  # реверс

my_list3 = [[6,7][8,9]]
print(my_list3[1][0])

for i in my_list:
    print(i)    # перебирает сами значения

for i in my_list3:
    for j in i:
        print(j)

for i in range(len(my_list)):
    print(i)    # перебирает индексы

for i in range(len(my_list)):
    print(my_list[i])    # перебирает сами значения и можно менять

new_list = []
new_list = my_list.copy()
new_list = my_list[:]  # то же самое, но не работает со вложенными массивами
print(new_list)
print(new_list)
from copy import deepcopy   # для вложенных списков
new_list = deepcopy(my_list3)

## Tuple - кортеж - нельзя менять, можно перебрать
my_tuple.count
my_tuple.index

new_list = list(my_tuple)

print(*my_tuple)

## Set - множество
# неиндексируемый и неупорядоченный
# элементы уникальные
new_list = list(my_set)
words = {'Hi', 'Hello', 'Bye'}
word = 'Hi'
if word in words:
    print(f'Слово {word} есть в списке {words}')

word1 =  {'Hi', 'Hello', 'Bye'}
word2 = {'Hi!', 'Hi','Hi?'}
print(word1.union(word2))
print(word1.difference(word2))
print(word1.isdisjoint(word2))


## Dictionary - словарь
new_list = list(my_dict)  # только индексы

print(my_dict.get(2))
my_dict[6] = 'six'
print(my_dict.get(6))

for i in my_dict:
    print(i)  # печатются ключи

for i in my_dict.keys:
    print(i)  # печатются ключи

for i in my_dict.values:
    print(i)  # печатются значения

for i, j in my_dict.items():
    print(i, j)  # печатаются ключи и значения

my_dict1 = {'one': 1, 'two': 2, 'three': 3}
my_dict2 = {'four': 4, 'five': 25, 'three': 333}
my_dict1.update(my_dict2)  # объединит и заменит

for i in  my_dict1.keys:
    if my_dict1.get(i) and my_dict2.get(i):
        my_dict1[i] = my_dict1.get(i) + my_dict2.get(i)

# Задайте строку из набора чисел. Напишите программу, которая 
# покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
string = input('Введите числа через пробел: ')
string = string.split(' ')

# Не по задаче:
my_list = []
while True:
    string = input('ghj')
    for i in string:
        if not i.isdigit():
            break
    else:
        if string != '':
            my_list.append(int(string))
        else:
            break
print(my_list)

# Задача:
string = input('Введите числа через пробел: ')
string = string.strip().split(' ')  # strip отрубает в начале и в конце лабуду
for i in range(len(string)):
    string[i] = int(string[i])
# дальше найти max



# Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.
nums = input('Введите числа через пробел: ')
nums = nums.strip().split(' ')
for i in range(len(nums)):
    nums[i] = int(nums[i])

# найти max_num

for i in range(max_num, nums[0]*nums[1]+1):
    if i % nums[0] == 0 and i % nums[1] == 0:
        print(i)
        break

# Другое решение:
k = 1
while min(*nums)*k%max(*nums) != 0:
    k += 1

print(max(*nums)*k)

nums = list(map(int, nums))   # перевести в int

# Найдите корни квадратного уравнения 'Ax² + Bx + C = 0' с помощью 
# математических формул нахождения корней квадратного уравнения
# надо распарсить строку
# a*x**2 + b*x + c = 0
# a = 
# b = 
# c =
string = '12*x**2 + 5*x + 7 = 0'
string = string.replace(' ', '')
print(string)
string = string[:-2].split('+')
print(string)
new_equation = []
for item in string:
    new_equation.append(item.split('*x')[0])
print(new_equation)
a, b, c = new_equation

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')


import random
equation = ''
koef = [0] * 3
for i in range(len(koef)):
    koef[i] = (random.randint(0,5))
print(koef)



# if koef[i] == 0:
#     equation = f'{koef[1]}*x + {koef[2]} = 0'
# else:
#     equation = f'{koef[0]}*x**2 + {koef[1]}*x + {koef[2]} = 0'

print(equation)


size = int(input('Введите max степень: '))
koef = {}
for i in range(size+1):
    koef[i] = random.randint(0,5)
print(koef)

equation = ''
for i in range(size, -1, -1):
    if koef[i] != 0:
        equation += f'{koef[i]}*x**{i} + '
    elif koef[i] == 1:
        equation += f'{koef[i]}*x + '
    elif i == 0:
        equation +=f'{koef[i]}' 
    else:
        equation += f''