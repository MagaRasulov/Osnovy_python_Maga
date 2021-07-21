# task 1
'''1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать
функцию type() для проверки типа. Элементы списка можно не запрашивать
у пользователя, а указать явно, в программе.'''

# my_list = []
# my_list.append('Привет')
# my_list.append(22)
# my_list.append(False)
# my_list.append(2.5)
# for i in my_list:
#     print(f'У элемента строки <({i})> тип {type(i)}')


# task 2
''' 2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При 
нечетном количестве элементов последний сохранить на своем месте. Для 
заполнения списка элементов необходимо использовать функцию input(). '''

# my_list = input('Введите значение для заполнения списка через запятую ').split(',')
# print(f'Это введенные вами значения {my_list}')
# i = 0
# while i < len(my_list):
#     try:
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#     except IndexError:
#         break
#     i += 2
# print(f'Это сделал PYTHON {my_list}')


#task 3
'''3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому 
времени года относится месяц (зима, весна, лето, осень). Напишите решения через 
list и через dict.'''

# what_month = int(input('Какой месяц? '))
# month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
#          'Август', 'Сентяюрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# if what_month == 12 or what_month == 1 or what_month == 2:
#     print(f'Ваш месяц {month[what_month-1]}, время года - "ЗИМА"')
# elif what_month == 3 or what_month == 4 or what_month == 5:
#     print(f'Ваш месяц {month[what_month - 1]}, время года - "ВЕСНА"')
# elif what_month == 6 or what_month == 7 or what_month == 8:
#     print(f'Ваш месяц {month[what_month - 1]}, время года - "ЛЕТО"')
# elif what_month == 9 or what_month == 10 or what_month == 11:
#     print(f'Ваш месяц {month[what_month - 1]}, время года - "ОСЕНЬ"')
#
# month_dict = {
#     1: 'Январь',
#     2: 'Февраль',
#     3: 'Март',
#     4: 'Апрель',
#     5: 'Май',
#     6: 'Июнь',
#     7: 'Июль',
#     8: 'Август',
#     9: 'Сентяюрь',
#     10: 'Октябрь',
#     11: 'Ноябрь',
#     12: 'Декабрь'
# }
# if what_month == 12 or what_month == 1 or what_month == 2:
#     print(f'Ваш месяц {month_dict[what_month]}, время года - "ЗИМА"')
# elif what_month == 3 or what_month == 4 or what_month == 5:
#     print(f'Ваш месяц {month_dict[what_month]}, время года - "ВЕСНА"')
# elif what_month == 6 or what_month == 7 or what_month == 8:
#     print(f'Ваш месяц {month_dict[what_month]}, время года - "ЛЕТО"')
# elif what_month == 9 or what_month == 10 or what_month == 11:
#     print(f'Ваш месяц {month_dict[what_month]}, время года - "ОСЕНЬ"')


#task 4
'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если 
слово длинное, выводить только первые 10 букв в слове.'''

# user_list = input('Введите слова через ПРОБЕЛ ').split(' ')
# a = 1
# for i in user_list:
#     if len(i) > 10:
#         print(f'{a}. {i[:10]}')
#     else:
#         print(f'{a}. {i}')
#     a += 1


#task 5
'''5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор 
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент 
с тем же значением должен разместиться после них.'''

# my_list = [7, 5, 3, 3, 2]
# my_list.append(int(input('Введите новый элемент ')))
# print(sorted(my_list, reverse=True))


#task 6*
'''6. * Реализовать структуру данных «Товары». Она должна представлять собой список 
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть 
два элемента — номер товара и словарь с параметрами (характеристиками товара: название, 
цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. 
запрашивать все данные у пользователя.'''
# database = []
# name_dict = []
# price_dict = []
# quantity_dict = []
# dimension_dict = []
# i = True
# n = 1
# while i:
#     name_t = input('Введите наименование товара: ')
#     name_dict.append(name_t)
#     price = input('Введите цену на товар: ')
#     price_dict.append(price)
#     quantity = input('Введите количество товара: ')
#     quantity_dict.append(quantity)
#     dimension = input('Введите единицу измерения: ')
#     dimension_dict.append(dimension)
#     database.append(((n), {'название': name_t, 'цена': price,
#                            'количество': quantity, 'ед.': dimension}))
#     next_name = input('жми ENTER, чтобы продолжить; для выхода введите любое значение ')
#     if next_name:
#         i = False
#     n += 1
#
# b = 0
# while b < len(database):
#     print(database[b])
#     b += 1
#
# database_dict = {'название': name_dict, 'цена': price_dict,
#                  'количество': quantity_dict, 'ед.': dimension_dict}
# print(database_dict)




