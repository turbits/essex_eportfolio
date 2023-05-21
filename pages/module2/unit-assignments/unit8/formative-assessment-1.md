---
layout: page
permalink: /pages/module2/unit-assignments/unit8/formative-assessment-1.html
---

⬅️[Back](/pages/module2/unit-assignments/unit8/m2u8.html)

# Module 2: Unit 8: Formative Assessment 1

"Rearrange the code blocks below to create a recursive function that finds the sum of `n` integers. For example, `find_sum(5)` would add up the numbers 0 to 5. Note, you must use a docstring, and not all of the blocks will be used."

Answer:
The docstring wasn't indented correctly but otherwise the answer was correct.

```python
def find_sum(n):
  """Recursively calculate the sum of the first n numbers"""
  if n == 0:
    return 0
  else:
    return n + find_sum(n - 1)
```

Feedback:

Start off with the function header and docstring. The next line of code is the base case if n == 0:. Recursive functions return values, they do not print them. Ignore the code block that says print(0), and use return 0. Next is the else statement. There are two incorrect blocks for the recursive case. First, ignore the code block that says return(n - find_sum(n-1)). The function should find the sum, but this code block is subtracting from n. Also, the recursive function call should move n closer to the base case. Since the base case is 0, n should get smaller. Use the code block that says, return(n + find_sum(n-1)).
