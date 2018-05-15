from NFA import NFA
from Rules import Rules
from Handler import Handler
from Tokenizer import Tokenizer
from DefHandler import DefHandler
from DefTokenizer import DefTokenizer

class Lexical(object):
	def __init__(self, rulesFile, code = None):
		self.rules = Rules(rulesFile)
		self.expressions = self.rules.get_expressions()
		self.definitions = self.rules.get_definitions()
		self.keywords = self.rules.get_keywords()
		self.punctuations = self.rules.get_punctuations()

		self.insert_definitions_to_expressions(self.definitions, self.expressions)
		self.def_dict = self.expand_definitions(self.definitions)
		self.nfa = self.expressions_to_nfa(self.expressions)
		if code:
			self.tokens = self.analize(code)


	def insert_definitions_to_expressions(self, definitions, expressions):
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

	def expand_definitions(self, definitions):
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

		return values_dict

	def expressions_to_nfa(self, expressions):
		tokens_dict = {}

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
			nfa_dict[key] = nfa_stack.pop()

		nfa = handler.combine(nfa_dict)
		return nfa

	def analize(self, codefile):
		return self.__analize(codefile, self.punctuations, self.keywords, self.def_dict, self.nfa)

	def __analize(self, codefile, punctuations, keywords, definitions, nfa):
		tokens = []
		word = ''
		char_types = []
		with open(codefile, 'r') as file:
			for line in file:
				for char in line:
					if char in punctuations:
						if len(char_types) > 0:
							tokens.append(nfa.match(char_types))
							word = ''
							char_types = []
						tokens.append(char)
					elif char is ' ':
						if len(char_types) > 0:
							tokens.append(nfa.match(char_types))
							word = ''
							char_types = []
					else:
						word += char
						for key in definitions:
							definition = definitions[key]
							if char in definition:
								char_types.append(key)
					if word in keywords:
						tokens.append(word)
						word = ''
						char_types = []
					else:
						match = nfa.match([word])
						if match:
							tokens.append(match)
							word = ''
							char_types = []
		return tokens
