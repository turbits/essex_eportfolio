# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# RECURSION - FACTORIAL

def factorial(n):
    """Calculate factorial recursively"""
    if n <= 0:
        return 1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print "Factorial of 5"
print(factorial(5))
print "Factorial of 0"
print(factorial(0))
print "Factorial of -2 - will return 1 as it is not a valid input"
print(factorial(-2))

# Reading Question
"""
Under what circumstances does it make sense to use recursion?

Answer (Correct): Recursion works best when the solution is self-similar

Feedback:
Recursion works best when the solution is self-similar. That is, when the problem is broken down into smaller parts, and the smaller parts are a variation of the large problem.
"""
