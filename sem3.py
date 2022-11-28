# # Задайте список. Напишите программу, которая определит, 
# # присутствует ли в заданном списке строк некое число.
# my_list = ['dfgh234mnb4', 'kjhg987mnb345', 'kjh98', 'jhgf98']
# symbol = input('Введите символ: ')
# for item in my_list:
#     for char in item:
#         if char == symbol:
#             print(f'Символ {symbol} присутствует в строке {item}')
#             break
#     else:
#         print(f'Символ {symbol} НЕ присутствует в строке {item}')

# for item in my_list:
#     if symbol in item:
#         print(f'Символ присутствует в строке')
#         break
#     else:
#         print(f'Символ НЕ присутствует в строке')


# for item in my_list:
#     count = 0
#     for i in range(len(item)):
#         if symbol == item[i]:
#             count = 0
#         print(f'Символ {symbol} присутствует в строке {item}'
#                 f' на {i} позиции')
#         print(f'Символ {symbol} присутствует в строке {item}'
#                 f' {count} раз')
# #     else:
# #         print(f'Символ НЕ присутствует в строке')

# print(my_list)
# for i in range(len(my_list)):
#     my_list[i] = my_list[i].replace(f'{symbol}, "A"')
# print(my_list)

# string = 'asdfg'
# new_string = []
# for i in string:
#     new_string.append(i)
# print(string)

# string = 'kjhg'
# string = list(string)      # из строки в список
# print(string)
# string = ''.join(string)   # обратно из списка строку
# print(string)

# string = 'kjhg'
# string = list(string) 
# new_string = []
# for i in range(0, len(string), 2):
#     new_string.append(string[i] + string[i+1])
# print(new_string)

# string = 'kjhg'
# string = list(string)
# def my_join(list, separator):
#     new_string = ''
#     for i in list:
#         new_string += i + separator
#     return new_string[:-len(separator)]

# print(my_join(string, '---'))


## Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: False
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: False
# - список: [], ищем: "123", ответ: False

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# print(my_list)
# search_string = input('Введите символ: ')
# count = 0
# for i in range(len(my_list)):
#     if my_list[i] == search_string:
#         count += 1
#     if count == 2:
#         print(f'Искомое значение {search_string} находится на позиции {i}')
#         break
# else:
#     if count == 1:
#         print(f'Искомое значение {search_string} НЕ повторяется')
#     else:
#         print(f'Искомое значение {search_string} НЕ найдено')

# # Задача: Напишите программу, в которой пользователь будет задавать две строки, 
# # а программа - определять количество вхождений одной строки в другой.
# # со строками через срезы
text = 'Первое число - 1, второе число - 2, сумма 3 чи'
sub_text = input('Введите подстроку: ')
## print(text.count(sub_text))
count = 0
for i in range(len(text)):
    if text[i:i+len(sub_text)] == sub_text:
        count += 1
print(f'Подстрока {sub_text} встречается {count} раз(а)')



