from Token import Token

class DefTokenizer(object):
	def __init__(self, definition):
		self.definition = definition
		self.symbols = {'|': 'ALT', '+': 'PLUS', '-': 'MINUS'}
		self.current = 0
		self.length = len(definition)
		self.tokens = []
		self.part = self.get_token()
		self.parse()

	def get_token(self):
		if self.current < self.length:
			symbol = self.definition[self.current]
			self.current += 1
			if symbol not in self.symbols.keys():
				token = Token('SYMBOL', symbol)
			else:
				token = Token(self.symbols[symbol], symbol)
			return token
		else:
			return Token('NONE', '')

	def parse(self):
		self.__parse1()
		if self.part.name in ['ALT', 'MINUS']:
			token = self.part
			self.part = self.get_token()
			self.parse()
			self.tokens.append(token)

	def __parse1(self):
		self.__parse2()
		if self.part.value not in '|-':
			self.__parse1()
			self.tokens.append(Token('CONCAT', '.'))

	def __parse2(self):
		self.__parse3()
		if self.part.name in ['PLUS']:
			self.tokens.append(self.part)
			self.part = self.get_token()

	def __parse3(self):
		if self.part.name == 'SYMBOL':
			self.tokens.append(self.part)
			self.part = self.get_token()

	def get_tokens(self):
		return self.tokens
