# -*- coding: utf-8 -*-
#Jake Goodwin 2016
#pre defined stuff
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z']
alpha_applied = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
         'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z']
start_point = None
user_string = None
user_list = []
#function to iterate through a loop
def make_alpha(alphabet, alphabet_key, start_point):
    index = 0
    start_index = start_point
    Token = True
    while Token:
        alphabet_key[index] = alphabet[start_index]
        index = index + 1
        start_index = start_index + 1
        if start_index == (len(alphabet) - 1):
            start_index = 0
        elif start_index == start_point:
            Token = False
#apply the cifer to the user's input
def encrypt_string(alphabet, alphabet_key, user_input):
    for index in range(len(user_input)):#might not need the -1
        for i in range(len(alphabet)):
            if user_input[index] == alphabet[i]:
                user_input[index] = alphabet_key[i]
                continue
#converting a string into a list
def string_to_list(string, user_list):
    for i in string:
        user_list.append(i)
#main beef of the program, the heart if you will...
print(alpha_applied)
make_alpha(alpha, alpha_applied, int(input('Please enter a shift:')))
print(alpha_applied)
user_string = input('please enter your message:')
string_to_list(user_string, user_list)
user_input = len(user_list)
print(user_list)
print(len(user_list))
encrypt_string(alpha, alpha_applied, user_list)
print(user_list)
