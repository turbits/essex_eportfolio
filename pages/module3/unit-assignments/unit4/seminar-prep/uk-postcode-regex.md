---
layout: page
permalink: /pages/module3/unit-assignments/unit4/seminar-prep/uk-postcode-regex.html
---

⬅️[Back](/pages/module3/unit-assignments/unit4/seminar-prep/seminar-preparation.html)


## Unit 4: Seminar Preparation: UK Postcode Regex

See below the code block for an output example.

### 🧑‍💻 Code

```python
import re


def validate_uk_postcode(postcode):
    # regex pattern for UK postcode validation
    pattern = "^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}$"
    
    # compile the regex pattern
    regex = re.compile(pattern)
    
    # check if postcode matches the pattern
    if regex.match(postcode):
        print(f"{postcode} - PASS")
    else:
        print(f"{postcode} - FAIL")


# use the function against the provided test cases, these should pass as far as i can tell
# https://ideal-postcodes.co.uk/guides/uk-postcode-format
print("\nShould pass:")
validate_uk_postcode("M1 1AA")
validate_uk_postcode("M60 1NW")
validate_uk_postcode("CR2 6XH")
validate_uk_postcode("DN55 1PT")
validate_uk_postcode("W1A 1HQ")
validate_uk_postcode("EC1A 1BB")

# use the function against test cases that should fail
print("\nShould fail:")
validate_uk_postcode("ZZZZZ 1")
validate_uk_postcode("123 123")
validate_uk_postcode("MA19 F12")
validate_uk_postcode("9AF B99")
validate_uk_postcode("X0A1 H0F")
```

### Output

```bash
$ python uk-postcode-regex.py
>
> Should pass:
> M1 1AA - PASS
> M60 1NW - PASS
> CR2 6XH - PASS
> DN55 1PT - PASS
> W1A 1HQ - PASS
> EC1A 1BB - PASS
>
> Should fail:
> ZZZZZ 1 - FAIL
> 123 123 - FAIL
> MA19 F12 - FAIL
> 9AF B99 - FAIL
> X0A1 H0F - FAIL
```
