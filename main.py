from NFA import NFA
from Rules import Rules
from Handler import Handler
from Tokenizer import Tokenizer
from DefHandler import DefHandler
from DefTokenizer import DefTokenizer

rules = Rules('rules.txt')

expressions = rules.get_expressions()
definitions = rules.get_definitions()
keywords = rules.get_keywords()
punctuations = rules.get_punctuations()

for key in definitions:
	definition = definitions[key]
	if '-' not in definition:
		for e_key in expressions:
			expression = expressions[e_key]
			if key in expression:
				new_expression = []
				for value in expression:
					if key == value:
						for new_value in definition:
							new_expression.append(new_value)
					else:
						new_expression.append(value)
				expressions[e_key] = new_expression

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

stack = []
def_handler = DefHandler()
values_dict = {}

for key in def_tokens_dict:
	values = []
	tokens = def_tokens_dict[key]
	for token in tokens:
		def_handler.handlers[token.name](token, stack, values)
	values_dict[key] = values

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
print nfa.match(['digit', 'digit'])
