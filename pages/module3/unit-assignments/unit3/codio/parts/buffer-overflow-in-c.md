---
layout: page
permalink: /pages/module3/unit-assignments/unit3/codio/parts/buffer-overflow-in-c.html
---

⬅️[Back](/pages/module3/unit-assignments/unit3/codio/m3u3-codio.html)

## Module 3: Unit 3: Codio Activity 1: Buffer Overflow in C

The instructions were to "click the rocket icon" which doesn't exist, to compile and run the bufoverflow.c file and observe the output. The rocket in the Codio UI must have been replaced with "Compile & Run" at some point since, which upon clicking resulted in the following output:

```
gcc -o && ./
gcc: error: missing filename after '-o'
gcc: fatal error: no input files
compilation terminated.
```

So instead I compiled and ran the file using the following command:

```
gcc ./bufoverflow.c -o bufoverflow && ./bufoverflow
```

Which resulted in the program compiling and running:

```
bufoverflow.c: In function ‘main’:
bufoverflow.c:8:5: warning: implicit declaration of function ‘gets’; did you mean ‘fgets’? [-Wimplicit-function-declaration]
     gets(buf);               // read from stdio (sensitive function!)
     ^~~~
     fgets
/tmp/cc6vNTqc.o: In function `main':
bufoverflow.c:(.text+0x3c): warning: the `gets' function is dangerous and should not be used.
Enter name: Trevor
Trevor
```

The second part of the activity was to run the code a second time and trigger a stack buffer overflow by putting in a string of "10 or more characters". This should, ideally, read as "9 or more characters" to prevent any confusion that 10 characters would be somehow required to trigger a buffer overflow in this example. Given that we are initialising an 8 character buffer, inputting a string above 8 characters long would result in a buffer overflow.

The compiler (gcc in this case) adds what are called "canaries" or protection variables that have known values. A value that is greater than the known value would result in a SIGABRT (abort signal), terminating the process with an error code indicating a stack smashing detection (stack buffer overflow) (Narang, P. 2022). I did this and the output was predictably as follows:

```
Enter name: 1234567890
1234567890
*** stack smashing detected ***: <unknown> terminated
Aborted (core dumped)
```

## References

- Narang, P. (2022) What is the "Stack Smashing Detected" Error? Available at: https://www.scaler.com/topics/stack-smashing-detected/ [Accessed 17 February 2023]
