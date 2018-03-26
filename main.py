from NFA import NFA
from Rules import Rules
from Tokenizer import Tokenizer

rules = Rules('rules.txt')

expressions =  rules.get_expressions()
# print expressions
for key in expressions:
	tokenizer = Tokenizer(expressions[key])

# print rules.get_definitions()
# print rules.get_keywords()
# print rules.get_punctuations()