from NFA import NFA
from Rules import Rules

rules = Rules('rules.txt')

expressions =  rules.get_expressions()
# print expressions
for key in expressions:
	nfa = NFA(key, expressions[key])

# print rules.get_definitions()
# print rules.get_keywords()
# print rules.get_punctuations()