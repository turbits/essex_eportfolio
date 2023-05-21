---
layout: page
permalink: /pages/module3/unit-assignments/unit5/equivalence-testing-in-python.html
---

⬅️[Back](/pages/module3/unit-assignments/unit5/m3u5.html)

### Module 3: Unit 3: Codio Activity: Equivalence Testing in Python

#### Assignment Instructions

Run equivalence.py in the Codio workspace - Testing with Python - which is an implementation of equivalence partitioning. This test partitions integers [-3,5] into equivalence classes based on `lambda x, y: (x-y)%4 == 0`.

In the output, you should be able to see how a set of objects to be partitioned are considered, and a function evaluates if the two objects are equivalent before printing the result.

test_equivalence_partition() produces the following output:

`set([1, -3]) set([2, -2]) set([3, -1]) set([0, 4]) 0 : set([0, 4]) 1 : set([1, -3]) 2 : set([2, -2]) 3 : set([3, -1]) 4 : set([0, 4]) -2 : set([2, -2]) -3 : set([1, -3]) -1 : set([3, -1])`


You should carry out further investigations on the code and experiment with it.

Remember to record your results, ideas and team discussions in your e-portfolio.

#### 🤔 My Reflections


##### Default Run of equivalence.py

codio@kansaslegacy-diagramsantana:~/workspace$ python equivalence.py 

ran with `range(-3, 5)`

```python
set([1, -3])
set([2, -2])
set([3, -1])
set([0, 4])
(0, ':', set([0, 4]))
(1, ':', set([1, -3]))
(2, ':', set([2, -2]))
(3, ':', set([3, -1]))
(4, ':', set([0, 4]))
(-2, ':', set([2, -2]))
(-3, ':', set([1, -3]))
(-1, ':', set([3, -1]))
```

##### Modifying the range

codio@kansaslegacy-diagramsantana:~/workspace$ python equivalence.py 

ran with `range(-3, 10)`

```python
set([1, 9, -3, 5])
set([2, 6, -2])
set([3, -1, 7])
set([0, 8, 4])
(0, ':', set([0, 8, 4]))
(1, ':', set([1, 9, -3, 5]))
(2, ':', set([2, 6, -2]))
(3, ':', set([3, -1, 7]))
(4, ':', set([0, 8, 4]))
(5, ':', set([1, 9, -3, 5]))
(6, ':', set([2, 6, -2]))
(7, ':', set([3, -1, 7]))
(8, ':', set([0, 8, 4]))
(9, ':', set([1, 9, -3, 5]))
(-2, ':', set([2, 6, -2]))
(-3, ':', set([1, 9, -3, 5]))
(-1, ':', set([3, -1, 7]))
```
