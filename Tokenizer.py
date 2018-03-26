from Token import Token

class Tokenizer(object):
	def __init__(self, expression):
		self.expression = expression
		self.symbols = {'(':'LEFT_PAREN', ')':'RIGHT_PAREN', '*':'STAR', '|':'ALT', '.':'CONCAT', '+':'PLUS'}
		self.current = 0
		self.length = len(expression)
		self.tokens = []
		self.part = self.get_token()
		self.parse()

	def get_token(self):
		if self.current < self.length:
			symbol = self.expression[self.current]
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
		if self.part.name in ['ALT', 'CONCAT']:
			token = self.part
			self.part = self.get_token()
			self.parse()
			self.tokens.append(token)

	def __parse1(self):
		self.__parse2()
		if self.part.value not in ')|.':
			self.__parse1()
			self.tokens.append(Token('CONCAT', '.'))

	def __parse2(self):
		self.__parse3()
		if self.part.name in ['STAR', 'PLUS']:
			self.tokens.append(self.part)
			self.part = self.get_token()

	def __parse3(self):
		if self.part.name == 'LEFT_PAREN':
			self.part = self.get_token()
			self.parse()
			if self.part.name == 'RIGHT_PAREN':
				self.part = self.get_token()
		elif self.part.name == 'SYMBOL':
			self.tokens.append(self.part)
			self.part = self.get_token()

	def get_tokens(self):
		return self.tokens
