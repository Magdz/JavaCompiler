from NFA import NFA
from Rules import Rules
from Handler import Handler
from Tokenizer import Tokenizer
from DefTokenizer import DefTokenizer

rules = Rules('rules.txt')

expressions = rules.get_expressions()
definitions = rules.get_definitions()
keywords = rules.get_keywords()
punctuations = rules.get_punctuations()

tokens_dict = {}

for key in expressions:
	tokenizer = Tokenizer(expressions[key])
	tokens = tokenizer.get_tokens()
	tokens_dict[key] = tokens

def_tokens_dict = {}

for key in definitions:
	tokenizer = DefTokenizer(definitions[key])
	tokens = tokenizer.get_tokens()
	def_tokens_dict[key] = tokens

for key in def_tokens_dict:
	print key
	for token in def_tokens_dict[key]:
		print token

nfa_dict = {}
handler = Handler()
nfa_stack = []

for key in tokens_dict:
	tokens = tokens_dict[key]
	for token in tokens:
		handler.handlers[token.name](token, nfa_stack)
	assert len(nfa_stack) == 1
	nfa_dict[key] = nfa_stack.pop()

nfa = handler.combine(nfa_dict)

 

# nfa_test = nfa_dict['num']
print nfa.match(['-'])
