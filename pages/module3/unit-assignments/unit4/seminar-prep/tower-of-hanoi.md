---
layout: page
permalink: /pages/module3/unit-assignments/unit4/seminar-prep/tower-of-hanoi.html
---

⬅️[Back](/pages/module3/unit-assignments/unit4/seminar-prep/seminar-preparation.html)


# Unit 4: Seminar Preparation: Tower of Hanoi

See below the code block for an output example.

## Code

```python
import sys


def hanoi(num_disks, source, target, auxiliary, pegs):
    if num_disks > 0:
        # move n - 1 disks from source to aux peg, using target peg as auxiliary
        hanoi(num_disks - 1, source, auxiliary, target, pegs)

        # move nth disk from source to target peg
        pegs[target].append(pegs[source].pop())
        print(f"Move disk {num_disks} from {source} to {target}")
        print_pegs(pegs)

        # move n - 1 disks from aux to target peg using source peg as auxiliary
        hanoi(num_disks - 1, auxiliary, target, source, pegs)


def print_pegs(pegs):
    for peg_name, peg in pegs.items():
        print(f"{peg_name}: ", end="")
        for disk in peg:
            print(f"{disk * '*'} ", end="")
        print()


def print_moves(num_disks):
    total_moves = 2 ** num_disks - 1
    print("\nThe recursion limit for Python 3.11 is, as of writing, 1000.\nWe can also get the recursion limit by calling `sys.getrecursionlimit()`\nIt is also possible to set the recursion limit, but this is not recommended as it can cause a stack overflow.")
    print("The total number of moves for a Tower of Hanoi problem can be calculated using the formula: 2^n - 1, where n is the number of disks.")
    print("---------------------------------------------")
    print(f"Recursion limit: {sys.getrecursionlimit()}")
    print(f"Total moves: {total_moves}")


number_of_disks = int(input("Enter number of disks: "))
source_peg = "A"
target_peg = "B"
auxiliary_peg = "C"

pegs = {
    source_peg: [i for i in range(number_of_disks, 0, -1)],
    target_peg: [],
    auxiliary_peg: []
}

print("Initial state:")
print_pegs(pegs)
hanoi(number_of_disks, source_peg, target_peg, auxiliary_peg, pegs)
print_moves(number_of_disks)
```

## Output Example

```bash
$ python tower-of-hanoi.py
$ Enter number of disks: 4
> Initial state:
> A: **** *** ** *
> B:
> C:
> Move disk 1 from A to C
> A: **** *** **
> B:
> C: *
...

> The recursion limit for Python 3.11 is, as of writing, 1000.
> We can also get the recursion limit by calling `sys.getrecursionlimit()`
> It is also possible to set the recursion limit, but this is not recommended as it can cause a stack overflow.
> The total number of moves for a Tower of Hanoi problem can be calculated using the formula: 2^n - 1, where n is the number of disks.
> ---------------------------------------------
> Recursion limit: 1000
> Total moves: 15
```

## Output Example With 55 Disks (RecursionError)

```bash
$ python tower-of-hanoi.py
$ Enter number of disks: 55
> ...
> RecursionError: maximum recursion depth exceeded in comparison
```
