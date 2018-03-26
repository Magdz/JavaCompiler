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
		print self.part
		print self.expression
		if self.part.name == 'ALT':
			token = self.part
			self.part = self.get_token()
			self.parse()
			self.tokens.append(token)

	def get_tokens(self):
		return self.tokens()
