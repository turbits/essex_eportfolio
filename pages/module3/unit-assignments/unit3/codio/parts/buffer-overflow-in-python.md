---
layout: page
permalink: /pages/module3/unit-assignments/unit3/codio/parts/buffer-overflow-in-python.html
---

⬅️[Back](/pages/module3/unit-assignments/unit3/codio/m3u3-codio.html)

# Module 3: Unit 3: Codio Activity 1: Buffer Overflow in Python


## Requirements

Now carry out a comparison of this code with one in Python (Buffer Overflow in Python), following these instructions:

In the Codio workspace, you will be using the file called Overflow.py:

```python
buffer=[None]*10
for i in range (0,11):
    buffer[i]=7
print(buffer)
```

- Run your code using: Python overflow.py (or use the codio rocket icon). What is the result?

There is no rocket icon, but running this code produces:

$ py bufferoverflow.py 
```
Traceback (most recent call last):
  File "C:\dev\python_files\bufferoverflow.py", line 3, in <module>
    buffer[i] = 7
    ~~~~~~^^^
IndexError: list assignment index out of range
```

- Read about Pylint at http://pylint.pycqa.org/en/latest/tutorial.html
  - Install pylint using the following commands:
    - `pip install pylint` (in the command shell/ interpreter)
    - Run pylint on one of your files and evaluate the output:
    - `pylint your_file`
    - (Make sure you are in the directory where your file is located before running Pylint)
    - What is the result? Does this tell you how to fix the error above?

Running `pylint bufferoverflow.py` produces:

$ pylint bufferoverflow.py 
```
************* Module bufferoverflow
bufferoverflow.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 7.50/10
```

The error message is not helpful in relation to the out of range error; it also appears to be failing on the first thing that it considers an issue. I am running flake8 in my VSCode editor, and it is reporting several warnings:

```
missing whitespace around operator (E225) Ln 1 Col 7
missing whitespace around arithmetic operator (E226) Ln 1 Col 14
whitespace before '{' (E211) Ln 2 Col 15
missing whitespace after ',' (E231) Ln 2 Col 17
missing whitespace around operator (E225) Ln 3 Col 14
```

To fix the error, we would need to change the code to not attempt to assign a value to an index that is out of range. We can do this by changing the code to:

```python
buffer = [None] * 10
for i in range(0, 10):  # changing from 0, 11 to 0, 10 to avoid the error
    buffer[i] = 7
print(buffer)
```

The output is now:

$ py bufferoverflow.py
```
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
```
