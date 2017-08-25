# Use Python3.5+
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
    regex_string = '/\*[^(\*/)]*?("(.*)")*?[^(\*/)]*?\*/$'
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


def q5():
    """Generate the NFA for strings with at most one repeated digit."""
    states = ["q", "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"]
    repeat_states = ["p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"]
    symbols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    initial_state = states[0]
    final_states = states[1::] + repeat_states
    initial_transitions = [("q", x, final_states[x]) for x in symbols]
    transitions = list()
    for i in range(len(final_states)):
        for j in range(len(symbols)):
            # No transition for repitition
            if i != j:
                transitions.append((final_states[i], symbols[j], final_states[j]))
    for i in range(len(repeat_states)):
        for j in range(len(symbols)):
            # No transition for repitition
            if i != j:
                transitions.append((repeat_states[i], symbols[j], final_states[j]))
    repeat_transitions = [(final_states[x], x, repeat_states[x]) for x in symbols]

    NFA = {
        "Q": states + repeat_states,
        "Sigma": symbols,
        "Delta": initial_transitions + transitions + repeat_transitions,
        "Start State": initial_state,
        "F": final_states
    }
    return NFA


def NFA_printer(NFA):
    """Print NFA in redeable format."""
    transitions = NFA.pop("Delta")
    print('{')
    for key in NFA:
        if type(NFA[key]) is list and len(NFA[key]) > 10:
            print("\t'"+key+"': [", ", ".join(["'"+str(x)+"'" for x in NFA[key][0:10]])+',')
            print("\t\t"+", ".join(["'"+str(x)+"'" for x in NFA[key][10::]]), ']')
        else:
            print("\t'"+key+"':", NFA[key])
    print("\t'"+"Delta"+"': [", ", ".join([str(x) for x in transitions[0:10]])+',')
    i = 10
    while i < len(transitions):
        print("\t\t", ", ".join([str(x)for x in transitions[i:i+10]])+',')
        i += 10
    print(']')
    print('}')


if __name__ == "__main__":
    print("Running Q1...")
    query_1 = "aaaeisdsddffggfgfgodfdfdfddfu"
    print("Query 1 =", query_1, "Status =", q1(query_1), '\n')

    query_2 = "aiesdsddffggfgfgodfdfdfddfu"
    print("Query 2 =", query_2, "Status =", q1(query_2), '\n')

    print("Running Q2...")
    query_1 = "aaabbbccddhhhiikkmmmnnnnzzz"
    print("Query 1 =", query_1, "Status =", q2(query_1), '\n')

    query_2 = "aaaabbbbddddcccc"
    print("Query 2 =", query_2, "Status =", q2(query_2), '\n')

    print("Running Q3...")
    query_1 = '/*"*/"sddfgfhg*/'
    print("Query 1 =", query_1, "Status =", q3(query_1), '\n')

    query_2 = '/**/"sddfgfhg*/'
    print("Query 2 =", query_2, "Status =", q3(query_2), '\n')

    print("Running Q4...")
    NFA_printer(q4())

    print("Running Q5...")
    NFA_printer(q5())
