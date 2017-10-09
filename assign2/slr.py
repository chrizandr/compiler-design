#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""SLR parser for CD assignment."""


class SLRParser:
    """Class for SLR Parser."""

    def __init__(self):
        """Init."""
        self.grammar = list()
        self.new_grammar = list()
        self.terminals = list()
        self.variables = list()
        self.I_n = dict()
        self.shift_list = list()
        self.reduction_list = list()
        self.parse_table = list()
        self.rule_dict = dict()
        self.follow_dict = dict()
        self.SR = list()
        self.RR = list()
        self.last_derivation = list()

    def read_yacc(self, file_name):
        """Read grammar in yacc format and convert to common notation."""
        curr_var = ""

        rules = []
        grammar_file = open(file_name, "r")

        for line in grammar_file:
            if ':' in line:
                curr_var = line.split(':')[0].strip()
                rule = curr_var + '->' + line.split(':')[1].replace(" ", "").strip().strip(';')
                rules.append(rule)

            elif '|' in line:
                rule = curr_var + '->' + line.split('|')[1].replace(" ", "").strip().strip(';')
                rules.append(rule)

            elif ';' in line:
                continue

        return rules

    def read_grammar(self, file_name):
        """Read grammar from the file and find variable and terminals."""
        non_yacc_grammar = self.read_yacc(file_name)

        for prod in non_yacc_grammar:
            rule = prod.strip()
            self.grammar.append(rule)

            if rule[0] not in self.variables:
                self.variables.append(prod[0])

        for prod in self.grammar:
            for token in prod.strip().replace(' ', '').replace('->', ''):
                if token not in self.variables and token not in self.terminals:
                    self.terminals.append(token)

        for l in range(1, len(self.grammar) + 1):
            self.rule_dict[l] = self.grammar[l - 1]

    def create_augmented_grammar(self, file_name):
        """Augment the grammar with new variable."""
        self.read_grammar(file_name)

        if "'" not in self.grammar[0]:
            self.grammar.insert(0, self.grammar[0][0] + "'" + '->' + self.grammar[0][0])

        self.new_grammar = []
        for prod in self.grammar:
            for i in range(len(prod)):
                if prod[i] == ">":
                    new_prod = prod[0:i+1] + '.' + prod[i+1::]
                    self.new_grammar.append(new_prod)

    def closure(self, production, init=True):
        """Find the closure set for the given production."""
        closure_set = []

        current_pos = production.index('.')

        try:
            current_variable = production[current_pos + 1]
        except:
            return closure_set

        if current_variable in self.variables:
            for prod in self.new_grammar:
                if prod[0] == current_variable:
                    if not init:
                        if prod[1] != "'":
                            closure_set.append(prod)
                    else:
                        closure_set.append(prod)
        return closure_set

    def init_states(self, file_name):
        """Initialise the state 0."""
        self.create_augmented_grammar(file_name)

        state = []

        state.append(self.new_grammar[0])
        i = 0

        for prod in state:
            closure_set = self.closure(prod)
            for rule in closure_set:
                if rule not in state:
                    state.append(rule)

            self.I_n[i] = state

    def create_states_shift_list(self, file_name):
        """Create remaining states and shift entries in parse table."""
        self.init_states(file_name)

        symbols = self.variables + self.terminals

        i = 0
        current_state = 0

        while len(self.I_n) != current_state:
            for each_variable in symbols:
                state = []

                for rule in self.I_n[current_state]:
                    if rule[-1] == '.':
                        continue

                    index = rule.index('.')
                    if rule[index + 1] == each_variable:
                        new_rule = (rule + ' ')[:-1]
                        new_rule = new_rule.replace('.', '')
                        new_rule = new_rule[:index + 1] + '.' + new_rule[index + 1:]
                        state.append(new_rule)

                        for rule_ in state:
                            closure_set = self.closure(rule_, init=False)
                            for prod in closure_set:
                                if prod not in state:
                                    state.append(prod)

                if state:
                    if state not in self.I_n.values():
                        i += 1
                        self.I_n[i] = state

                    for (k, v) in self.I_n.iteritems():
                        if state == v:
                            idx = k
                    self.shift_list.append([current_state, each_variable, idx])

            current_state += 1

        self.parse_table += self.shift_list

    def find_first(self, var):
        """Find first set for the variable."""
        first_set = []

        for rule in self.rule_dict.values():
            variable, production = rule.split("->")
            if variable == var:
                if production[0] in self.terminals:
                    first_set.append(production[0])
                else:
                    first_set = first_set + self.find_first(production[0])
        return first_set

    def find_follow(self, var):
        """Find follow set for the variable."""
        follow_set = []
        if var == self.rule_dict[1][0]:
            follow_set.append("$")

        for rule in self.rule_dict.values():

            lhs, rhs = rule.split("->")

            if var == rule[-1]:
                if rule[0] != var:
                    for each in self.find_follow(rule[0]):
                        if each not in follow_set:
                            follow_set.append(each)

            if var in rhs[:-1]:
                idx = rhs.index(var)
                try:
                    if rhs[idx+1] in self.variables:
                        follow_set += self.find_first(rhs[idx+1])
                    else:
                        follow_set.append(rhs[idx+1])
                except:
                    pass

        return follow_set

    def find_reductions(self):
        """Add reductions to the parse table."""
        self.reduction_list.append([1, '$', 'Accept'])

        for item in self.I_n.iteritems():
            try:
                for each_production in item[1]:
                    (lhs, rhs) = each_production.split('.')

                    for rule in self.rule_dict.iteritems():

                        if lhs == rule[1]:
                            f = self.find_follow(lhs[0])

                            for each_var in f:
                                self.reduction_list.append([item[0], each_var, 'R' + str(rule[0])])
            except:
                pass
        self.parse_table += self.reduction_list

    def parser_print(self):
        """Print all details about the parser and grammar."""
        print '\n--------------------ORIGINAL GRAMMAR--------------------'
        for item in self.rule_dict.iteritems():
            print item

        print 'Terminals:', self.terminals
        print 'NonTerminals:', self.variables

        print '\n--------------------AUGMENTED GRAMMAR--------------------'
        for item in self.new_grammar:
            print item.replace('.', '')

        print '\n--------------------LR(0) STATES--------------------'
        for item in self.I_n.iteritems():
            print item

        print '\n--------------------PARSE TABLE--------------------'
        for item in self.parse_table:
            s1, s2, s3 = item
            if s2 in self.terminals and type(s3) is int:
                print '[%s, %s, %s]' % (s1, s2, 'S'+str(s3))
            else:
                print '[%s, %s, %s]' % (s1, s2, str(s3))
        print

    def parse(self, file_name):
        """Parse the given grammar."""
        self.create_states_shift_list(file_name)
        self.find_reductions()
        self.parser_print()

    def test_string(self, string):
        """Test a given string to be valid for the grammar."""
        self.last_derivation = []

        assert string[-1] != '$'
        string = string + '$'
        done = False
        stack = []
        stack.append(0)

        print '''STACK\t\tSTRING\t\tACTION'''
        while not done:
            Reduce = False
            Shift = False
            for reduction in self.reduction_list:

                if reduction[0] == int(stack[-1]) and reduction[1] == string[0]:
                    Reduce = True
                    print ''.join(str(p) for p in stack), '\t\t', string, '\t\t', 'Reduce', reduction[2]

                    if reduction[2] == 'Accept':
                        return True

                    var = self.rule_dict[int(reduction[2][1])]
                    (lhs, rhs) = var.split('->')

                    for x in range(len(rhs)):
                        stack.pop()
                        stack.pop()

                    self.last_derivation.append(var)

                    var = lhs
                    stack.append(var)

                    for a in self.parse_table:

                        if a[0] == int(stack[-2]) and a[1] == stack[-1]:
                            stack.append(str(a[2]))
                            break

            for shift in self.shift_list:

                if shift[0] == int(stack[-1]) and shift[1] == string[0]:
                    Shift = True
                    print ''.join(str(p) for p in stack), '\t\t', string, '\t\t', 'Shift', 'S' + str(shift[2])
                    stack.append(string[0])
                    stack.append(str(shift[2]))
                    string = string[1:]

            if not Reduce and not Shift:
                print ''.join(str(p) for p in stack), '\t\t', string
                return False

    def print_last_derivation(self):
        """Print the right derivation for the last tested string."""
        steps = len(self.last_derivation)
        var, result = self.last_derivation[steps-1].strip().split('->')
        try:
            assert var == self.rule_dict[1][0]
        except AssertionError:
            print "Not a valid string"
            exit(0)

        print "\n------------------RIGHT MOST DERIVATION------------------------\n"

        print var, "=>",
        string = result

        for i in range(steps-2, -1, -1):
            print string, "=>",
            prod = self.last_derivation[i]
            var, result = prod.strip().split('->')
            for j in range(len(string)-1, -1, -1):
                if string[j] == var:
                    string = string[:j] + result + string[j+1::]
                    break
        print string
        print "\n---------------------------------------------------------------\n"


if __name__ == '__main__':
    intro_text = """\n\t\tThis is an implementation of the SLR(1) parser.\n\t\tDone by Chris Andrew of UG4 for Compilers course."""

    print intro_text
    string = raw_input('''\n\nEnter filename where grammar is stored: \n''')
    file_name = string.strip()

    parser = SLRParser()
    parser.parse(file_name)

    string = raw_input('''Enter Test String: ''')

    print '\nTest String:', string
    print

    result = parser.test_string(string)

    if result is True:
        print '\n---ACCEPTED---\n'
        parser.print_last_derivation()

    else:
        print '\n---NOT ACCEPTED---\n'
