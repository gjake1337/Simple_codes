# -*- coding: utf-8 -*-
#Jake Goodwin 2016
#pre defined stuff
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z']
alpha_applied = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
         'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z']
start_point = None
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
print(alpha_applied)
make_alpha(alpha, alpha_applied, 12)
print(alpha_applied)
