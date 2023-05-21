def recursion_test(n):
    if n == 0:
        return
    else:
        print(n)
        recursion_test(n - 1)


recursion_test(10000)
# this will throw a `RecursionError: maximum recursion depth exceeded in comparison` error
