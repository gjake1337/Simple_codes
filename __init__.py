# -*- coding: utf-8 -*-
#Jake Goodwin 2016
#pre defined stuff
alpha = 'abcdefghijklmnopqrstuvwyxz'
alpha_applied = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 
'f': None, 'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None,
'm': None, 'n': None, 'o': None, 'p': None, 'q': None, 'r': None, 's': None,
't': None, 'u': None, 'v': None, 'w': None, 'y': None, 'x': None, 'z': None}
print(alpha_applied['a'])
userinput = input('Please enter your plain text:')
#pull out the index of the value given for the alphabet
def pullout(IV):
    index = 0
    for i in alpha:
        if i == IV:
           return index
           break
        else:
            index = index + 1
#applying the shift to the key/ dict data structure
def shift_alphabet(alphabet_key, alphabet):
    shift_index = input("please enter a shift:")
    for i in alphabet_key:
        print(i, shift_index)
        alphabet_key[i] = alphabet[shift_index]
        shift_index = shift_index + 1
        if shift_index == len(alphabet) - 1:
            shift_index = 0
        elif alphabet_key[i] == alphabet[shift_index]:
            print('function finished')
            break
shift_alphabet(alpha_applied, alpha)
print(alpha_applied)
