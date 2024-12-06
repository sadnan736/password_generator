import string
import random
from string import printable, whitespace


def take_int_input():
    try: return int(input(''))
    except ValueError:
        print('Please a non negative, non fractional integer value:\n')
        return take_int_input()

def passphrase_gen():
    return 0

def element_gen():
    numb_choice = input('Include letters? y/n\n').lower()
    # make function until correction input given
    sp_chr_choice = input('Include letters? y/n:\n').lower()
    # use function until correction input given

    elements = []
    elements += list(string.ascii_letters)
    if numb_choice == 'y':
        elements += list(string.digits)
    if sp_chr_choice == 'y':
        elements += list(set(string.printable) - set(string.whitespace) - set(string.digits) - set(string.ascii_letters))

    return elements




type_pass = input("Would you like a [1] 'Passphrase' (random string of words) or [2] 'Password' (random string of characters? 1/2:\n").lower()

if type_pass == 'passphrase' or type_pass =='1':
    pass_w = passphrase_gen()
elif type_pass == 'password' or type_pass == '2':
    print('How long should the password be? (positive-non fractional integer value)\n')
    length_of_pass = take_int_input()

    password_elements = element_gen()
    password = ''
    for i in range(length_of_pass):
        password += random.choice(password_elements)

print(f'Your password is:\n{password}')

