---
layout: page
permalink: /pages/module6/unit-assignments/unit6/m6u6-codio-activity.html
---

⬅️[Back](/pages/module6/unit-assignments/unit6/m6u6.html)

# Unit 6: Codio Activity - pytest

This codio activity had us copy some code into a file, `wallet.py`, `test_wallet.py`, and run pytest against the `test_wallet` file, `pytest -q test_wallet.py`.

These are the two files it had us create:

```python
# wallet.py

class InsufficientAmount(Exception):
    pass 


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount


    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount


    def add_cash(self, amount):
        self.balance += amount
```

```python
# test_wallet.py

import pytest

from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
```

The output of the pytest command was:

```bash
codio@phantomsheriff-videofrog:~/workspace$ pytest -q test_wallet.py 
-bash: pytest: command not found
codio@phantomsheriff-videofrog:~/workspace$ 
```

Very cool! At this point I ditched codio, because it's complete garbage, and ran these locally while following the "guide" in codio. In fact, you'll find the code to this activity in this unit's location in the repository: `pages/module6/unit-assignments/unit6/codio-activity`, [here](https://github.com/turbits/essex_eportfolio/blob/main/pages/module6/unit-assignments/unit6/codio-activity).

After installing pytest and creating the files locally and running the tests I got:

`$ pytest -q test_wallet.py`

```bash
$ pytest -q test_wallet.py
.....                                                                                                            [100%]
5 passed in 0.02s
```

Great! All tests passed. The activity then had us amend the tests so they fail, and that was the end of the activity. I did so:


```python
# test_wallet_fail.py

import pytest

from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 182480


def test_setting_initial_amount():
    wallet = Wallet(1)
    assert wallet.balance == 100


def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(123)
    assert wallet.balance == 100


def test_wallet_spend_cash():
    wallet = Wallet(2)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(0)
```

Running pytest on our fail test file: `$ pytest -q test_wallet_fail.py`

```bash
FFFFF                                                                                                            [100%]
====================================================== FAILURES =======================================================
_____________________________________________ test_default_initial_amount _____________________________________________

    def test_default_initial_amount():
        wallet = Wallet()
>       assert wallet.balance == 182480
E       assert 0 == 182480
E        +  where 0 = <wallet.Wallet object at 0x000002505EC1F070>.balance

test_wallet_fail.py:8: AssertionError
_____________________________________________ test_setting_initial_amount _____________________________________________

    def test_setting_initial_amount():
        wallet = Wallet(1)
>       assert wallet.balance == 100
E       assert 1 == 100
E        +  where 1 = <wallet.Wallet object at 0x000002505EBDA6E0>.balance

test_wallet_fail.py:13: AssertionError
________________________________________________ test_wallet_add_cash _________________________________________________

    def test_wallet_add_cash():
        wallet = Wallet(10)
        wallet.add_cash(123)
>       assert wallet.balance == 100
E       assert 133 == 100
E        +  where 133 = <wallet.Wallet object at 0x000002505EC1E170>.balance

test_wallet_fail.py:19: AssertionError
_______________________________________________ test_wallet_spend_cash ________________________________________________

    def test_wallet_spend_cash():
        wallet = Wallet(2)
>       wallet.spend_cash(10)

test_wallet_fail.py:24:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <wallet.Wallet object at 0x000002505EBDBAF0>, amount = 10

    def spend_cash(self, amount):
        if self.balance < amount:
>           raise InsufficientAmount('Not enough available to spend {}'.format(amount))
E           wallet.InsufficientAmount: Not enough available to spend 10

wallet.py:12: InsufficientAmount
___________________________ test_wallet_spend_cash_raises_exception_on_insufficient_amount ____________________________

    def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
        wallet = Wallet()
>       with pytest.raises(InsufficientAmount):
E       Failed: DID NOT RAISE <class 'wallet.InsufficientAmount'>

test_wallet_fail.py:30: Failed
=============================================== short test summary info ===============================================
FAILED test_wallet_fail.py::test_default_initial_amount - assert 0 == 182480
FAILED test_wallet_fail.py::test_setting_initial_amount - assert 1 == 100
FAILED test_wallet_fail.py::test_wallet_add_cash - assert 133 == 100
FAILED test_wallet_fail.py::test_wallet_spend_cash - wallet.InsufficientAmount: Not enough available to spend 10
FAILED test_wallet_fail.py::test_wallet_spend_cash_raises_exception_on_insufficient_amount - Failed: DID NOT RAISE <class 'wallet.InsufficientAmount'>
5 failed in 0.07s
```
