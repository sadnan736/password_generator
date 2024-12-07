import string
import random


def take_int_input():
    try: return int(input(''))
    except ValueError:
        print('Please a non negative, non fractional integer value:\n')
        return take_int_input()

def passphrase_element_gen():
    numb_choice = input('Include letters in between words? y/n\n').lower()
    # make function until correction input given
    sp_chr_choice = input('Include special character in between words? y/n:\n').lower()
    # make function until correction input given
    elements_list = []

    if numb_choice == 'y':
        numb_choice = 1
        elements_list.append(list(string.digits))
    else:
        numb_choice = 0

    if sp_chr_choice == 'y':
        sp_chr_choice = 1
        elements_list.append(list(set(string.printable)-set(string.ascii_letters)-set(string.digits)-set(string.whitespace)))
    else:
        sp_chr_choice = 0
    return numb_choice + sp_chr_choice , elements_list


def password_element_gen():
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
# make function until correction input given

if type_pass == 'passphrase' or type_pass =='1':
    print('How many words should the passphrase be? (positive-non fractional integer value)')
    length_of_pass = take_int_input()

    between_chars, pass_elements = passphrase_element_gen()
    user_pass = ''

    with open('words_alpha.txt', 'r') as file:
        english_words = file.read().split()

    for i in range(length_of_pass):
        user_pass += random.choice(english_words)
        for _ in range(random.randint(0,between_chars)):
            user_pass += random.choice(random.choice(pass_elements))


elif type_pass == 'password' or type_pass == '2':
    print('How long should the password be? (positive-non fractional integer value)\n')
    length_of_pass = take_int_input()

    pass_elements = password_element_gen()

    user_pass = ''
    for i in range(length_of_pass):
        user_pass += random.choice(pass_elements)
else:
    user_pass = ''
print(f'Your password is:\n{user_pass}')

