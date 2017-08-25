# ----------------------------------------------------------
# Here is the solutions to the first question
# All the regex are writing for each question below, there are python functions defined that use the regex to check the string
# The functions are called in the main function with a few examples
#
#  Q1 = [^aeiou]*?a[^eiou]*?e[^aiou]*?i[^aeou]*?o[^aeiu]*?u[^aeio]*?$
#
#  Q2 = a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*q*x*y*z*$
#
#  Q3 = '/\*[^(\*/)]*?("(.*)")*?[^(\*/)]*?\*/'
#
#  Q4 =
#
#  Q5 =
# ----------------------------------------------------------

"""Question one, reular expressions written in Python."""

import re
import json


def q1(string):
    """Strings of lower case that contain the vowels in order."""
    regex_string = str("[^aeiou]*?" + "a" +
                       "[^eiou]*?" + "e" +
                       "[^aiou]*?" + "i" +
                       "[^aeou]*?" + "o" +
                       "[^aeiu]*?" + "u" +
                       "[^aeio]*?" + "$")

    print(regex_string)

    regex = re.compile(regex_string)
    matchObj = re.match(regex, string)

    return matchObj is not None


def q2(string):
    """Strings of lower case in ascending lexographic order."""
    alphabet = "abcdefghijklmnopqrstuvwqxyz"

    regex_string = "".join([x+"*" for x in alphabet]) + "$"
    print(regex_string)

    regex = re.compile(regex_string)
    matchObj = re.match(regex, string)

    return matchObj is not None


def q3(string):
    """Strings surrounded by /* */ without intervening */ unless in ("")."""
    regex_string = '/\*[^(\*/)]*?("(.*)")*?[^(\*/)]*?\*/'
    print(regex_string)

    regex = re.compile(regex_string)
    matchObj = re.match(regex, string)

    return matchObj is not None


def q4():
    """Generate the NFA for strings with no repeated digits."""
    states = ["q", "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"]
    symbols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    initial_state = states[0]
    final_states = states[1::]
    initial_transitions = [("q", x, final_states[x]) for x in symbols]
    transitions = list()
    for i in range(len(final_states)):
        for j in range(len(symbols)):
            # No transition for repitition
            if i != j:
                transitions.append((final_states[i], symbols[j], final_states[j]))

    NFA = {
        "Q": states,
        "Sigma": symbols,
        "Delta": initial_transitions + transitions,
        "Start State": initial_state,
        "F": final_states
    }
    return NFA


def q5(string):
    """All strings with at most one repeated digit."""
    pass


if __name__ == "__main__":
    print(q3('/*"*/"sddfgfhg*/'))
    print(json.dumps(q4(), indent=4))
