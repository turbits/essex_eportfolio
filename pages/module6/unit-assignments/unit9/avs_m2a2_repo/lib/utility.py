# +===================================================================+
# utility.py - helper functions
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

prompt = "$"


def c_err(code, msg):
    """Returns a formatted string based on the code and message provided"""
    print("ERROR: {}\nREASON: {}".format(code, msg))
    return


def raw_input(param: str):
    return param


def get_choice(choice_list):
    for count, value in enumerate(choice_list):
        print("{}: {}".format(count, value))

    user_input: str = raw_input("{} ".format(prompt))
    if user_input == 'q':
        return 'q'
    for count, value in enumerate(choice_list):
        # isalnum() checks if the supplied argument is alphanumeric
        if not str.isalnum(user_input):
            c_err("AVS-FRO-USER", "Invalid choice, please try again")
            return ""
        elif user_input == value:
            return value.lower().strip()
        elif int(user_input) == count:
            return int(count)
    # print c_err("AVS-FRO-USER", "Invalid choice, please try again")
    return get_choice(choice_list)
