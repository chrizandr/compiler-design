Solutions to Assignment 1
=====================
The Questions for the assignment can be found in the `.pdf` file.
The solutions for the questions are given below.

-------
### Question 1

__NOTE__: Each of these regular expressions can be evaluated using the `q1.py` file where functions to match Strings with each of these expressions have been defined.

------
**a.** Strings of lower case that contain the vowels in order.

The following regular expression will be able to detect strings for the given problem.
```
[^aeiou]*?a[^eiou]*?e[^aiou]*?i[^aeou]*?o[^aeiu]*?u[^aeio]*?$
```

----
**b.** Strings of lower case in ascending lexographic order.

The following regular expression will be able to detect strings for the given problem.
```
a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*q*x*y*z*$
```

---
**c.** Strings surrounded by `/*` and `*/` without intervening `*/` unless in `""`.

The following regular expression will be able to detect strings for the given problem.
```
'/\*[^(\*/)]*?("(.*)")*?[^(\*/)]*?\*/'
```
__NOTE__: `*` is a special character in regular expressions and as such an escape character is used before it. `\*` is the same as the `*` character.

---
**d.** Strings with no repeated digits.

The given problem will require a DFA with around `10!` states, such a DFA is not easily represented and the regular expression to represent the same will be very complex. A small modification will allow us to simplify the problem such that no two consecutive digits are same. This will allow `0102` to pass, but will not allow `0012` to pass.

The following NFA defined in the standard notation can be used to accept such strings
```python
{   "Q": ["q", "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"],
    "Sigma": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Start state": "q",
    "F": ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"],
    "Transitions":
    [
        ('q', 0, 'q0'), ('q', 1, 'q1'), ('q', 2, 'q2'), ('q', 3, 'q3'), ('q', 4, 'q4'), ('q', 5, 'q5'), ('q', 6, 'q6'), ('q', 7, 'q7'), ('q', 8, 'q8'), ('q', 9, 'q9'),
        ('q0', 1, 'q1'), ('q0', 2, 'q2'), ('q0', 3, 'q3'), ('q0', 4, 'q4'), ('q0', 5, 'q5'), ('q0', 6, 'q6'), ('q0', 7, 'q7'), ('q0', 8, 'q8'), ('q0', 9, 'q9'),
        ('q1', 0, 'q0'), ('q1', 2, 'q2'), ('q1', 3, 'q3'), ('q1', 4, 'q4'), ('q1', 5, 'q5'), ('q1', 6, 'q6'), ('q1', 7, 'q7'), ('q1', 8, 'q8'), ('q1', 9, 'q9'),
        ('q2', 0, 'q0'), ('q2', 1, 'q1'), ('q2', 3, 'q3'), ('q2', 4, 'q4'), ('q2', 5, 'q5'), ('q2', 6, 'q6'), ('q2', 7, 'q7'), ('q2', 8, 'q8'), ('q2', 9, 'q9'),
        ('q3', 0, 'q0'), ('q3', 1, 'q1'), ('q3', 2, 'q2'), ('q3', 4, 'q4'), ('q3', 5, 'q5'), ('q3', 6, 'q6'), ('q3', 7, 'q7'), ('q3', 8, 'q8'), ('q3', 9, 'q9'),
        ('q4', 0, 'q0'), ('q4', 1, 'q1'), ('q4', 2, 'q2'), ('q4', 3, 'q3'), ('q4', 5, 'q5'), ('q4', 6, 'q6'), ('q4', 7, 'q7'), ('q4', 8, 'q8'), ('q4', 9, 'q9'),
        ('q5', 0, 'q0'), ('q5', 1, 'q1'), ('q5', 2, 'q2'), ('q5', 3, 'q3'), ('q5', 4, 'q4'), ('q5', 6, 'q6'), ('q5', 7, 'q7'), ('q5', 8, 'q8'), ('q5', 9, 'q9'),
        ('q6', 0, 'q0'), ('q6', 1, 'q1'), ('q6', 2, 'q2'), ('q6', 3, 'q3'), ('q6', 4, 'q4'), ('q6', 5, 'q5'), ('q6', 7, 'q7'), ('q6', 8, 'q8'), ('q6', 9, 'q9'),
        ('q7', 0, 'q0'), ('q7', 1, 'q1'), ('q7', 2, 'q2'), ('q7', 3, 'q3'), ('q7', 4, 'q4'), ('q7', 5, 'q5'), ('q7', 6, 'q6'), ('q7', 8, 'q8'), ('q7', 9, 'q9'),
        ('q8', 0, 'q0'), ('q8', 1, 'q1'), ('q8', 2, 'q2'), ('q8', 3, 'q3'), ('q8', 4, 'q4'), ('q8', 5, 'q5'), ('q8', 6, 'q6'), ('q8', 7, 'q7'), ('q8', 9, 'q9'),
        ('q9', 0, 'q0'), ('q9', 1, 'q1'), ('q9', 2, 'q2'), ('q9', 3, 'q3'), ('q9', 4, 'q4'), ('q9', 5, 'q5'), ('q9', 6, 'q6'), ('q9', 7, 'q7'), ('q9', 8, 'q8')
    ]
}
```



### Question 2
------
