---
layout: page
permalink: /pages/module2/assignment3/unit8/recursion-factorial.html
---

⬅️[Back](/pages/module2/assignment3/unit8/m2a3u8.html)

## Module 2: Assignment 3: Unit 8: Recursion Factorial

### Code

```python
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
```

### Output:

```
Factorial of 5
120
Factorial of 0
1
Factorial of -2 - will return 1 as it is not a valid input
1
```
