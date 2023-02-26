brothers = ["Aibulat", "Salavat", "Ильяс", "Airas", "Azat", "Ilfir", "Айсылу"]
data = "Салам"
data.upper()
print(data.upper())
print(brothers)
brothers.sort(reverse=True)
print(brothers)
# data = "Python developer"
# # for name in brothers:
# #     print(f"Hello, {name}!")
#
#
# # print(len(brothers))
# # print(brothers[0])
# # print(brothers)
# # brothers.pop(0)
# # print(brothers)
# # print(len(brothers))
# while len(brothers):
#     print(f"Salam {brothers[0]}")
#     # print(brothers)
#     brothers.pop(0)
#     # print(len(brothers))
#
# print(f"Ostatok v spiske {brothers}")



# Программа принимает на вход натуральное число N. Ваша задача: вывести на экран все числа от 1 до N, каждое число на отдельной строке.
# a = int(input())
# for i in range(1, a+1):
#     print(i)

# Напишите программу, которая выведет все элементы арифметической прогрессии от 0 до 500 включительно с шагом 5.
# Каждый элемент выводится отдельно на своей строке в таком виде
# for i in range(0, 501, 5):
#     print(i)

# Программа принимает на вход натуральное число N. Ваша задача: вывести на экран все числа от N до 1 в сторону уменьшения,
# каждое число на отдельной строке.
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# «Надо было брать биткоин в 2012!» именно такую фразу ваша программа должна вывести на экран 13 раз
# Программа должна вывести 13 раз фразу «Надо было брать биткоин в 2012!», каждый раз на отдельной строке и без кавычек.
# text = "Надо было брать биткоин в 2012!"
# for i in range(1, 14):
#     print(text, i)

# Давайте и мы напишем подобную программу. На вход ей будет поступать фраза и затем количество раз,
# которое эту фразу нужно повторить.
# text = input()
# count = int(input())
# for i in range(0, count):
#     print(text)

# Напишите программу, которая считывает два натуральных числа a и b (гарантируется, что a<b), после чего для всех чисел от a до b включительно выводит:
# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.
# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Давайте составим сводную информацию о квадратах и кубах интервала чисел.
# На вход программе подается два натуральных числа a и b (гарантируется, что a<b), после чего для каждого целого числа на интервале от a до b включительно
# необходимо вывести фразу следующего вида: «Число {число}; его квадрат = {квадрат}; его куб = {куб}»
# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     print(f"Число {i}; его квадрат = {i ** 2}; его куб = {i ** 3}")







# y_start = int(input())
# y_finish = int(input())
# x_start = int(input())
# x_finish = int(input())
#
#
# line_x = []
#
# for x in range(x_start, x_finish+1):
#     line_x.append(x)
#
# print(line_x)
