# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# RECURSION - FIBONACCI

def fibonacci(n):
    """Calculate Fibonacci numbers"""
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
      
print "Fibonacci of 3"
print(fibonacci(3))
print "Fibonacci of 0"
print(fibonacci(0))
print "Fibonacci of 8"
print(fibonacci(8))
print "Fibonacci of 30"
print(fibonacci(30))

print "Fibonacci sequence of 10"      
fibonacci_length = 10
for num in range(fibonacci_length):
    print(fibonacci_seq(num))

print "Fibonacci sequence of 30"
fibonacci_length = 30
for num in range(fibonacci_length):
    print(fibonacci_seq(num))

print "Fibonacci sequence of 50 - will timeout"
fibonacci_length = 50
for num in range(fibonacci_length):
    print(fibonacci_seq(num))

# Reading Question
"""
What is the purpose of the base case in recursion?

Answer (Correct): When true, the base case stops the recursive calls and returns a value.

Feedback:
When true, the base case stops the recursive calls and returns a value. In the example of factorial, the base case is when n is less than or equal to 1. The function returns 1 and the long line of multiplication happens.
"""
