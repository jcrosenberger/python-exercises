from operator import truediv
import os
def clear_console():
    os.system('clear')
clear_console()


# ██████╗░███████╗░██████╗░██╗███╗░░██╗  ███████╗██╗░░██╗███████╗██████╗░░█████╗░██╗░██████╗███████╗
# ██╔══██╗██╔════╝██╔════╝░██║████╗░██║  ██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝
# ██████╦╝█████╗░░██║░░██╗░██║██╔██╗██║  █████╗░░░╚███╔╝░█████╗░░██████╔╝██║░░╚═╝██║╚█████╗░█████╗░░
# ██╔══██╗██╔══╝░░██║░░╚██╗██║██║╚████║  ██╔══╝░░░██╔██╗░██╔══╝░░██╔══██╗██║░░██╗██║░╚═══██╗██╔══╝░░
# ██████╦╝███████╗╚██████╔╝██║██║░╚███║  ███████╗██╔╝╚██╗███████╗██║░░██║╚█████╔╝██║██████╔╝███████╗
# ╚═════╝░╚══════╝░╚═════╝░╚═╝╚═╝░░╚══╝  ╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝╚═════╝░╚══════╝

####################################################################################################
#######################################       ONE       ############################################
####################################################################################################

def is_two(test_true):
    if test_true == 2 or test_true == '2':
        return True
    else:
        return False

print(is_two(input('Pick a number.\n')))


####################################################################################################
#######################################       TWO       ############################################
####################################################################################################

def is_vowel(test_true):
    vowels = ['a','e','i','o','u']
    if test_true.lower() in vowels:
        return True
    else:
        return False

print(is_vowel(input('Pick a letter.\n')))


####################################################################################################
#######################################      THREE      ############################################
####################################################################################################

def is_consonant(test_true):
    a=test_true
    #is_vowel(a)
    if is_vowel(a) == False:
        return True
    else:
        return False

print(is_consonant(input('Pick a letter.\n')))
    
####################################################################################################
#######################################       FOUR      ############################################
####################################################################################################
    
def cap_first_letter(some_word):
    if is_consonant(some_word[0]) == True:
        returned = some_word[0].upper()
        returned +=(some_word[1:len(some_word)])
        return returned
    else:
        return False

print(cap_first_letter(input('Type a word please.\n')))
####################################################################################################
#######################################       FIVE      ############################################
####################################################################################################
    
