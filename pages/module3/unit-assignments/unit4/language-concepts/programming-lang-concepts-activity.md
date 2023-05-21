---
layout: page
permalink: /pages/module3/unit-assignments/unit4/language-concepts/programming-lang-concepts-activity.html
---

⬅️[Back](/pages/module3/unit-assignments/unit4/m3u4.html)

## Unit 4: Programming Language Concepts Activity

### 📝 Requirements

Read Larson (2018) and Weidman (n.d.) then answer the questions below, adding them as evidence to your e-portfolio. You may want to complete this activity in conjunction with or after completing Seminar 2 preparation.

- What is ReDOS and what part do ‘Evil Regex’ play?
- What are the common problems associated with the use of regex? How can these be mitigated?
- How and why could regex be used as part of a security solution?

### 🤔 Reflection

1. What is ReDOS and what part do "Evil Regex" play?

ReDoS is a type of denial of service attack that involves exploiting the regex naive algorithm to overload the finite state machine, called a nondeterministic finite automation, or NFA. The overloading of this NFA can cause the regex engine to hang, crash, or consume excessive resources, which can lead to a denial of service style attack (Weidman, n.d.).

"Evil Regex" are regular expressions that allow this kind of attack, such as `([a-zA-Z]+)*`. This regular expression is vulnerable to ReDoS because it is unbounded, meaning it can match an infinite number of strings if the right input is provided.

2. What are the common problems associated with the use of regex? How can these be mitigated?

Common issues associated with regex that would lead to a ReDoS would be incorrect character sets, mismatched or unbalanced parenthesis, braces, or quotes, wildcards, and line anchors (Larson, 2018). These issues can be mitigated by using a regex syntax checker, such as [ACRE](http://fac-staff.seattleu.edu/elarson/web/regex.htm) or [regexr](https://regexr.com/).

3. How and why could regex be used as part of a security solution?

Regex can be used in many ways, but the most obvious way is to use it to validate user input. Validating user input via regex is an efficient way to ensure input is in the correct format, and to prevent attacks such as SQL injection.

Regex can also be used to ensure passwords meet minimum length and/or complexity requirements, restrict character input, identify patterns in spam emails or malicious code, validate or replace personally identifiable information (PII) such as credit card numbers, social insurance numbers, addresses, and much more.


### ✒️ References

- Weidman, A. (n.d.) Regular expression Denial of Service - ReDoS. Available at: [https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS) [Accessed 27 March 2023]
- Larson, E. (2018) Automatic Checking of Regular Expressions. Available at: [http://fac-staff.seattleu.edu/elarson/web/Research/acre.pdf](http://fac-staff.seattleu.edu/elarson/web/Research/acre.pdf) [Accessed 27 March 2023]

