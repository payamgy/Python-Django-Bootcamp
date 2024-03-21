
# ///////////////////////////////////////////////////////Q 06/////////////////////////////////////////////////////
# import random

#
# def game():
#     user_count = 0
#     computer_count = 0
#     for i in range(3):
#         computer_choice = str(random.choice(("r", "p", "s")))
#         print((computer_choice))
#
#         user_choice = str(input("Please select one of the options r/p/s. "))
#
#         if user_choice in ('r', 'p', 's'):
#             if computer_choice == user_choice:
#                 continue
#             else:
#                 if (computer_choice == "r") and (user_choice == "p"):
#                     user_count += 1
#                 elif computer_choice == "p" and user_choice == "s":
#                     user_count += 1
#                 elif computer_choice == "s" and user_choice == "r":
#                     user_count += 1
#                 else:
#                     computer_count += 1
#         else:
#             print("wrong choice!")
#
#         print(f"user: {user_count} computer: {computer_count}")
#     count_user_win = 0
#     count_computer_win = 0
#
#     if user_count == computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "Tie")
#         return 2
#
#     elif user_count > computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "// User wins.")
#         return 0
#
#     elif user_count < computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "// computer wins.")
#         return 1
#
#
# flag = True
# total_computer_wins = 0
# total_user_wins = 0
# total_tie = 0
#
# while flag:
#     a = game()
#     if a == 1:
#         total_computer_wins += 1
#     elif a == 0:
#         total_user_wins += 1
#     elif a == 2:
#         total_tie += 1
#
#     user_flag = input("Do you want to play again? ")
#     if user_flag.lower() != 'yes':
#         flag = False
#
# empty_dict = {}
# if total_user_wins > total_computer_wins:
#     print("User won!")
#     empty_dict.update({'user': total_user_wins})
#
# elif total_user_wins < total_computer_wins:
#     print("Computer won!")
#     empty_dict.update({'computer': total_computer_wins})
# else:
#     print("tie")
#     empty_dict.update({'tie': total_tie})
#
# print(empty_dict)


# ///////////////////////////////////////////////////////Q 07/////////////////////////////////////////////////////
# We are American!
# my_dict = {
#     '0': 'zero',
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine',
#     '10': 'ten',
#     '11': 'eleven',
#     '12': 'twelve',
#     '13': 'thirteen',
#     '14': 'fourteen',
#     '15': 'fifteen',
#     '16': 'sixteen',
#     '17': 'seventeen',
#     '18': 'eighteen',
#     '19': 'nineteen',
#     '20': 'twenty',
#     '30': 'thirty',
#     '40': 'forty',
#     '50': 'fifty',
#     '60': 'sixty',
#     '70': 'seventy',
#     '80': 'eighty',
#     '90': 'ninety',
#     '100': 'hundred'
# }
#
# numbers_to_ten = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
# #
# # l = s.split()
# # print(l)
# # for num in l:
# #     if num.isnumeric():
# #         print(convert_to_numbers(num))
#
# user_input = str(int(input("Please enter a number. ")))
# my_num = list(str(user_input))
# counter = len(my_num)
# # for i in my_num:
# # print(my_num)
# # print(my_dict[my_num[0]])
# # print(my_dict[str(my_num[0])])
#
# if counter == 3:
#     if my_num[1] == '1':
#         double_digit = my_dict.get(str("".join(my_num[1:])))
#         print(f"{my_dict[my_num[0]]} hundred and {double_digit}")
#
#     elif my_num[1] == '0' and my_num[2] == '0':
#         print(f"{my_dict[my_num[0]]} hundred")
#
#     elif my_num[1] == '0' and my_num[2] != '0':
#         print(f"{my_dict[my_num[0]]} hundred {my_dict[my_num[2]]}")
#
#     elif my_num[2] == '0':
#         print(f"{my_dict[my_num[0]]} hundred and {my_dict[str(10 * int(my_num[1]))]}")
#     else:
#         print(f"{my_dict[my_num[0]]} hundred and {my_dict[str(10 * int(my_num[1]))]} {my_dict[my_num[2]]}")
#
# elif counter == 2:
#     if my_num[0] == '1':
#         print(my_dict.get(str(user_input)))
#
#     elif my_num[1] == '0':
#         print(f"{my_dict.get(str(user_input))}")
#
#     else:
#         print(f"{my_dict[str(10 * int(my_num[0]))]} {my_dict[my_num[1]]}")
# elif counter == 1:
#     print(f"{my_dict[my_num[0]]}")


# ///////////////////////////////////////////////////////Q 08/////////////////////////////////////////////////////
# import random
#
#
# def game():
#     user_count = 0
#     computer_count = 0
#     for i in range(3):
#         computer_choice = str(random.choice(("r", "p", "s")))
#         print((computer_choice))
#
#         user_choice = str(input("Please select one of the options r/p/s. "))
#
#         if user_choice in ('r', 'p', 's'):
#             if computer_choice == user_choice:
#                 continue
#             else:
#                 if (computer_choice == "r") and (user_choice == "p"):
#                     user_count += 1
#                 elif computer_choice == "p" and user_choice == "s":
#                     user_count += 1
#                 elif computer_choice == "s" and user_choice == "r":
#                     user_count += 1
#                 else:
#                     computer_count += 1
#         else:
#             print("wrong choice!")
#
#         print(f"user: {user_count} computer: {computer_count}")
#
#     if user_count == computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "Tie")
#         return 2
#
#     elif user_count > computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "// User wins.")
#         return 0
#
#     elif user_count < computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "// computer wins.")
#         return 1
#
#
# user_answer = input("Do you want to continue the previous game?")
# if user_answer == 'yes':
#     file = open('res.txt', 'r')
#     content = file.read()
#     list_a = content.split(",")
#     total_computer_wins = int(list_a[0])
#     total_user_wins = int(list_a[1])
#     total_tie = int(list_a[2])
#     empty_dict = {'computer': int(list_a[0]), 'user': int(list_a[1]), 'tie': int(list_a[2])}
#     print(content)
#     file.close()
# else:
#     empty_dict = {'computer': 0, 'user': 0, 'tie': 0}
#     file = open("res.txt", "w")
#     file.write(f"{str((empty_dict.get('computer')))},{str((empty_dict.get('user')))},{str((empty_dict.get('tie')))}")
#     file.close()
#     total_computer_wins = 0
#     total_user_wins = 0
#     total_tie = 0
#
# flag = True
# while flag:
#     a = game()
#     if a == 1:
#         total_computer_wins += 1
#     elif a == 0:
#         total_user_wins += 1
#     elif a == 2:
#         total_tie += 1
#
#     user_flag = input("Do you want to play again? ")
#     if user_flag.lower() != 'yes':
#         flag = False
#
# if total_user_wins > total_computer_wins:
#     print("User won!")
#
# elif total_user_wins < total_computer_wins:
#     print("Computer won!")
# else:
#     print("tie")
#
#
# empty_dict.update({'user': total_user_wins})
# empty_dict.update({'computer': total_computer_wins})
# empty_dict.update({'tie': total_tie})
#
# file = open("res.txt", "w")
# file.write(f"{str((empty_dict.get('computer')))},{str((empty_dict.get('user')))},{str((empty_dict.get('tie')))}")
# file.close()


# ///////////////////////////////////////////////////////Q 09/////////////////////////////////////////////////////
#
#
# def merge_dicts(dict1, dict2):
#
#     merged_dict = dict1.copy()
#
#     for key, value in dict2.items():
#         if key in merged_dict:
#             merged_dict[key] += value
#         else:
#             merged_dict[key] = value
#
#     return merged_dict
#
#
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'b': 200, 'd': 400, 'a': 300}
#
# combined_dict = merge_dicts(d1, d2)
# print(combined_dict)



# Q9
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'b': 200, 'd': 400, 'a': 300}
#
# d3 = {}
# print(d1.keys())
# for i in d1.keys():
#     for j in d2.keys():
#         print(i, j)
#         if i == j:
#             temp = d1.get(i) + d2.get(j)
#             d3[i] = temp
#             # print(temp)
#         else:
#             if i not in d2.keys():
#                 d3[i] = d1.get(i)
#             elif j not in d1.keys():
#                 d3[j] = d2.get(j)
#
# print(d3)
# ///////////////////////////////////////////////////////Q 010/////////////////////////////////////////////////////
# Sample_Data = [{"V": "S001"}, {"V": "S002"},
#                {"VI": "S001"}, {"VI": "S005"},
#                {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
