# task 1
''' 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''
# a = int(input('Введите делимое '))
# b = int(input('Введите делитель '))
# def zero(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#         b = int(input('Введите делитель отличный от нуля '))
#         return a / b
# print(zero(a, b))


# task 2
''' 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры 
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''
# us_name = input('Имя ')
# us_surname = input('Фамилия ')
# us_date = input('Год рождения ')
# us_city = input('Город проживания ')
# us_email = input('Email ')
# us_phone = input('Телефон ')
# def database(a, b, c, d, e, f):
#     return (f'{b} {a}, родился {c} г., проживает в г.{d}; почта: {e}; телефон: {f}')
# print(database(a=us_name, b=us_surname, c=us_date, d=us_city, e=us_email, f=us_phone))


# task 3
''' 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает 
сумму наибольших двух аргументов.'''
# def my_func(a, b, c):
#     maxim = sorted([a, b, c], reverse=True)
#     summ = int(maxim[0]) + int(maxim[1])
#     return summ
#
# print(my_func(9, 100, 7))


# task 4
''' 4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде 
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения 
числа в степень. Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень 
с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая 
использование цикла.'''
# def my_func(x, y):
#     return x**y
#
# print(my_func(5, -1))

# def my_func(x, y):
#     i = 1
#     decision = x
#     while i < abs(y):
#         decision *= x
#         i += 1
#     return 1 / decision
# print(my_func(10, -3))


# task 5
''' 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо
числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен
после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после
этого завершить программу.'''
# summ = 0
# n = True
# while n:
#     try:
#         user_str = (input('Введите числа в строчку ').split())
#         for i in user_str:
#             summ += int(i)
#         print(summ)
#     except ValueError:
#         print(summ)
#         print('Вы не хотите вводить числа, тогда я не хочу дальше считать')
#         break


# task 6
''' 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую 
его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое 
слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().'''
# def int_func(text):
#     return text.title()
#
# user_str = input('Введите строку из слов в нижнем регистре ')
# print(int_func(user_str))


