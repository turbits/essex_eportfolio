---
layout: page
permalink: /pages/module3/unit-assignments/unit7/python-shell.html
---

⬅️[Back](/pages/module3/unit-assignments/unit7/m3u7.html)

## Unit 7: Python Shell

Assignment questions and answers to follow.

### 🧑‍💻 Code

```python
import os
import sys


def list_directory():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    print("Contents of the current directory:")
    for file in files:
        print(file)


def add_numbers(a, b):
    result = a + b
    print(f"Result: {result}")


def show_help():
    print("Available commands:")
    print("LIST - List the contents of the current directory")
    print("ADD a b - Add two numbers together (a and b)")
    print("HELP - Show the list of available commands")
    print("EXIT - Exit the shell")


def main():
    while True:
        command = input("Enter a command: ").strip()
        command_parts = command.split()

        if command_parts[0].upper() == "LIST":
            list_directory()
        elif command_parts[0].upper() == "ADD":
            if len(command_parts) == 3:
                try:
                    a = float(command_parts[1])
                    b = float(command_parts[2])
                    add_numbers(a, b)
                except ValueError:
                    print("Invalid input. Please provide two numbers.")
            else:
                print("Invalid input. ADD command expects two numbers.")
        elif command_parts[0].upper() == "HELP":
            show_help()
        elif command_parts[0].upper() == "EXIT":
            print("Exiting shell...")
            sys.exit(0)
        else:
            print("Invalid command. Type HELP for a list of available commands.")


if __name__ == "__main__":
    main()

```

### 🤔 Questions

1. What are the two main security vulnerabilities with your shell?
    - The shell is vulnerable to code injection. We are not sanitising the "input()" function
    - The shell allows anyone to run commands without authentication or authorization.

2. What is one recommendation you would make to increase the security of the shell?
    - Implement authentication and authorization mechanism to restrict access to the shell.

3. Add a section to your e-portfolio that provides a (pseudo) code example of changes you would make to the shell to improve its security.
    - I'll answer this with real Python code, albeit a very simple example. It is worth noting that this code is Python 3.x.

```python
import getpass


def authenticate_user(username, password):
    # check if creds provided are valid
    if username == "admin" and password == "supersecret":
        return True
    else:
        return False


def main():
    # prompt for creds
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # authenticate user
    if not authenticate_user(username, password):
        print("Invalid credentials. Exiting...")
        sys.exit(1)

# ... the rest of the code
```
