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


def q4(string):
    """Strings surrounded by /* */ without intervening */ unless in ("")."""
    regex_string = '/\*[^(\*/)]*?("(.*)")*?[^(\*/)]*?\*/'
    print(regex_string)

    regex = re.compile(regex_string)
    matchObj = re.match(regex, string)

    return matchObj is not None


if __name__ == "__main__":
    print(q3('/*"*/"sddfgfhg*/'))
