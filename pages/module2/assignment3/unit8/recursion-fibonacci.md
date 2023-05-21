---
layout: page
permalink: /pages/module2/assignment3/unit8/recursion-fibonacci.html
---

⬅️[Back](/pages/module2/assignment3/unit8/m2a3u8.html)

## Module 2: Assignment 3: Unit 8: Recursion Fibonacci

### Code

```python
# FIBONACCI NUMBER
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

```

### Output:

```
# FIBONACCI NUMBER OUTPUT
Fibonacci of 3
2
Fibonacci of 0
0
Fibonacci of 8
21
Fibonacci of 30
832040

# FIBONACCI SEQUENCE OUTPUT
Fibonacci sequence of 10
0
1
1
2
3
5
8
13
21
34
Fibonacci sequence of 30
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
Fibonacci sequence of 50
0
1
196418
317811
514229
832040
1346269
2178309
3524578
5702887
9227465
14930352
24157817
... (python times out)
```
