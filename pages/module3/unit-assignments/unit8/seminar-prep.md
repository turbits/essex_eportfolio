---
layout: page
permalink: /pages/module3/unit-assignments/unit8/seminar-prep.html
---

⬅️[Back](/pages/module3/unit-assignments/unit8/m3u8.html)

# Unit 8: Seminar Prep

Unit assignment code, questions, and answers to follow.

## Requirements

Read the Cryptography with Python blog at tutorialspoint.com (link is in the reading list). Select one of the methods described/ examples given and create a python program that can take a short piece of text and encrypt it.

Create a python program in Codio (you can use the Jupyter Notebooks space provided in the Codio resources section) that can take a text file and output an encrypted version as a file in your folder on the Codio system. Demonstrate your program operation in this week’s seminar session.

**Answer the following questions in your e-portfolio:**
- Why did you select the algorithm you chose?
- Would it meet the GDPR regulations? Justify your answer.
- We will review your work from Unit 7 (Python Shell) in this week’s seminar, as well as this cryptography activity. There will also be an opportunity to review your team’s assignment progress during the seminar.

Remember to record your results, ideas and team discussions in your e-portfolio and complete the Codio activities in Unit 7. 

**Learning Outcomes**
- Identify and manage security risks as part of a software development project.
- Critically analyse development problems and determine appropriate methodologies, tools and techniques (including program design and development) to solve them.
- Design and develop/adapt computer programs and to produce a solution that meets the design brief and critically evaluate solutions that are produced.

## Answer/Code

> Create a python program in Codio (you can use the Jupyter Notebooks space provided in the Codio resources section) that can take a text file and output an encrypted version as a file in your folder on the Codio system. Demonstrate your program operation in this week’s seminar session.

I chose not to use Codio as I can't attend seminars (time difference, they happen during my work day). I used a local Python 3.11 install on my Windows 11 machine. Since I implemented Fernet symmetric encryption and showed knowledge related to more complex encryption methods in [assignment 2](/pages/module3/assignment2/m3a2.md), I'm going to use a simple ROT13 encryption algorithm for this assignment.

**The code**

```python
import sys


def rot13encrypt(input):
    """
    Encrypts a string using ROT13 encryption.
    """
    output = ""
    for char in input:
        if char.isalpha():
            if char.isupper():
                output += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                output += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            output += char
    return output


def rot13decrypt(input):
    """
    Decrypts a string using ROT13 encryption.
    """
    output = ""
    for char in input:
        if char.isalpha():
            if char.isupper():
                output += chr((ord(char) - ord('A') - 13) % 26 + ord('A'))
            else:
                output += chr((ord(char) - ord('a') - 13) % 26 + ord('a'))
        else:
            output += char
    return output


def main():
    while True:
        print("\nROT13 Encryption/Decryption")
        print("===========================")
        print("Please choose a mode:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        mode = input("Mode: ")

        if mode == "1":
            input = input("Input: ")
            print("\nOutput: " + rot13encrypt(input))
        elif mode == "2":
            input = input("Input: ")
            print("\nOutput: " + rot13decrypt(input))
        elif mode == "3":
            sys.exit(0)
        else:
            print("\nInvalid mode")

main()
```

**The output**

```
$ py rot13.py

ROT13 Encryption/Decryption
===========================
Please choose a mode:
1. Encrypt
2. Decrypt
3. Exit
Mode: 1
Input: Trevor

Output: Geribe

ROT13 Encryption/Decryption
===========================
Please choose a mode:
1. Encrypt
2. Decrypt
3. Exit
Mode: 2
Input: Geribe

Output: Trevor
```


> Why did you select the algorithm you chose?

I chose ROT13 because of it's simplicity and because of its use as the canonical weak encryption algorithm. It is still interesting however, and it is a good example of a simple substitution cipher.


> Would it meet the GDPR regulations? Justify your answer.

Certainly not. ROT13 is often used as **the** example of a weak encryption algorithm, and is moreso used for puzzles and games. It is not suitable for any real-world use, but it is fun to use. 😊

