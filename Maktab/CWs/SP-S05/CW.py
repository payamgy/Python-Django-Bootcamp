# Q number 2
import math

# Return double of n
# def addition(n):
#     return n + n
#
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# Q number 2


# def capitalize_strings(text):
#     return text.title()
#
#
# strings = ['hello', 'world', 'python']
#
# result = list(map(capitalize_strings, strings))
# print(result)


# Q number 3

# def addition(n):
#     return n ** 2
#
#
# numbers = [1, 2, 3, 4, 5]
# result = map(addition, numbers)
# print(list(result))


# Q number 4
# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     new_string = ""
#     for char in string:
#         if char not in vowels:
#             new_string += char
#     return new_string
#
#
# strings = ['hello', 'world', 'python']
#
#
# result = map(remove_vowels, strings)
# print(list(result))


# # Q number 5
# def find_lengths(words):
#     return len(words)
#
#
# strings = ['hello', 'world', 'python']
# result = map(find_lengths, strings)
# print(list(result))
#
# result = map(lambda text: len(text), strings)
#
# print(list(result))


# Q number 6
# numbers = [1, 2, 3, 10]
#
#
# def check_even_odd(number):
#     new_list = list()
#     if number % 2 == 0:
#         new_list.append("even")
#     else:
#         new_list.append("odd")
#
#     return new_list
#
#
# result = map(check_even_odd, numbers)
# print(list(result))
#
# numbers = [1, 2, 3, 10]
# res = list((map(lambda number: "even" if (number % 2 == 0) else "odd", numbers)))
# print(res)

# Q number 7
# words = ["Hello", "World", "We", "Are", "Group one"]
#
#
# def reverse_strings(word):
#     return word[::-1]
#     # return "".join(sorted(word, reverse=True))
#
#
# res = map(reverse_strings, words)
# print(list(res))

# print(list(map(lambda x: x[::-1], words)))


# Q number 8

#
# def decimal_to_binary(n):
#     return bin(n).replace("0b", "")
#
#
# numbers = [12, 221, 10]
#
# res = map(decimal_to_binary, numbers)
# print(list(res))


# Q number 9

# def filter_long_words(strings, n):
#     new_test = list()
#     if len(strings) <= n:
#         new_test.append(strings)
#
#     return new_test

# n = int(input("n: "))
# words = ["Hellooooo", "World", "Python"]
# res = map(lambda x: filter_long_words(x, n), words)
# print(list(res))


# Q number 10
# def calculate_factorial(n):
#     return math.factorial(n)
#
#
# numbers = [3, 5, 10]
# res = map(calculate_factorial, numbers)
# print(list(res))

# Q number 11

# def filter_image_files(file_name):
#     file_name_sep = file_name.split(".")
#     return file_name_sep[-1]
#
#
# files_list = ["info.jpg", "readme.txt", "cat.gif"]
# res = filter(lambda x: True if filter_image_files(x) in ["jpg", "png", "gif"] else False, files_list)
# print(list(res))

# Q log
# master_dict = {}
#
# file = open(file='note.txt', mode="r")
# line_list = list()
#
# content = file.read().split("\n")
# i = 0
#
# method_list = list()
# status_list = list()
# total_request = len(content)
# size_list = list()
#
# for item in content:
#     line_list.append(item.split(" "))
#     method_list.append(line_list[i][5])
#     status_list.append(line_list[i][-2])
#     size_list.append(line_list[i][-1])
#     i += 1
#
# real_size_list = list()
# for item in size_list:
#     try:
#         real_size_list.append(int(item))
#     except Exception:
#         continue
#
# # Filter
# frequency_method_dict = dict()
# for word in set(method_list):
#     counter = method_list.count(word)
#     frequency_method_dict.update({word: counter})
#
# # Filter
# frequency_status_dict = dict()
# for word in set(status_list):
#     counter = status_list.count(word)
#     frequency_status_dict.update({word: counter})
#
# print(f"Total Requests: {total_request}")
# print("HTTP Methods: ")
# for k, v in frequency_method_dict.items():
#     print(f"\t {k}: {v}")
#
# print("HTTP Status Codes:")
# for k, v in frequency_status_dict.items():
#     print(f"\t {k}: {v}")
#
# print(f"Total Response Body Size: {sum(real_size_list)} bytes")

# Q number Log :)
#
# file = open(file='note.txt', mode="r")
# main_list = list()
#
# for line in range(11):
#     content = file.readline().split(" ")
#     for j in content:
#         main_list.append(j)
#
#
# frequency_dict = dict()
# for word in set(main_list):
#     counter = main_list.count(word)
#     if counter >= 1:
#         frequency_dict.update({word: counter})
#
#
# print(f"""
#
# Total Requests: {frequency_dict.get('-')/2}
# HTTP Methods:
#   GET: {frequency_dict.get('"GET')}
#   POST: {frequency_dict.get('"POST')}
#   ...
# HTTP Status Codes:
#   200: {frequency_dict.get('200')}
#   302: {frequency_dict.get('302')}
#   304: {frequency_dict.get('304')}
#   ...
# Total Response Body Size:-
# """)


# dynamic menu
# def complex(a, b):
#     return f'Complext Operaion {a} {b}'
#
#
# operations = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '/': lambda x, y: x / y,
#     'com': complex
#
# }
#
# while True:
#     x = input('enter op: ')
#     numbers = list(map(int, input().split()))
#
#     result = operations[x](numbers[0], numbers[1])
#     print(result)
#
#     # if x == '+':
#     #     ...
#     # if x == '-':
#     #     ...

#
# user_input = input().replace(" ", "")
#
# numbers_list = list()
# decimal_list = list()
# words_list = list()
#
#
# def f(text):
#     new_list = text.split(",")
#
#     for i in new_list:
#         if "." in i:
#             new_i = i.replace(".", "")
#             if new_i.isdigit():
#                 decimal_list.append(i)
#             else:
#                 words_list.append(i)
#
#         elif i.isnumeric():
#             numbers_list.append(int(i))
#
#         else:
#             words_list.append(i)
#
#
# f(text=user_input)
#
# print(numbers_list)
# print(decimal_list)
# print(words_list)
#
#
# types_dict = {"integers": {len(numbers_list)},
#               "floats": {len(decimal_list)},
#               "strings": {len(words_list)},
#               }
#
# for k,v in types_dict.items():
#     print(f"{k}: {v}")

# string1 = "123"
# string2 = "12.3"
# string3 = "١٢٣"
# string4 = "12.3a"
#
# print(string1.isnumeric())  # True
# print(string2.isnumeric())  # False
# print(string3.isnumeric())  # True
# print(string4.isnumeric())  # False
#
# print(string1.isdigit())  # True
# print(string2.isdigit())  # False
# print(string3.isdigit())  # True
# print(string4.isdigit())  # False
#
# print(string1.isdecimal())  # True
# print(string2.isdecimal())  # False
# print(string3.isdecimal())  # True
# print(string4.isdecimal())  # False



