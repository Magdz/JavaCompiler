from NFA import NFA
from Rules import Rules
from Handler import Handler
from Tokenizer import Tokenizer

rules = Rules('rules.txt')

tokens_dict = {}

expressions =  rules.get_expressions()
for key in expressions:
	tokenizer = Tokenizer(expressions[key])
	tokens = tokenizer.get_tokens()
	tokens_dict[key] = tokens

nfa_dict = {}
handler = Handler()
nfa_stack = []

for key in tokens_dict:
	tokens = tokens_dict[key]
	for token in tokens:
		handler.handlers[token.name](token, nfa_stack)
	assert len(nfa_stack) == 1
	nfa = nfa_stack.pop()
	nfa.set_key(key)
	nfa_dict[key] = nfa

nfa_test = nfa_dict['id']
print nfa_test.match(['letter', 'digit', 'letter'])

# print expressions
# print rules.get_definitions()
# print rules.get_keywords()
# print rules.get_punctuations()