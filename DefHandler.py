
class DefHandler(object):
	def __init__(self):
		self.handlers = {
			'SYMBOL': self.handle_symbol,
			'ALT': self.handle_alt,
			'PLUS': self.handle_plus,
			'MINUS': self.handle_minus
		}

	def handle_symbol(self, token, stack, values):
		stack.append(token.value)

	def handle_alt(self, token, stack, values):
		pass

	def handle_plus(self, token, stack, values):
		value = stack.pop()
		values.append(value)
		values.append(token.value)

	def handle_minus(self, token, stack, values):
		value2 = stack.pop()
		value1 = stack.pop()
		index = value1
		while index <= value2:
			values.append(index)
			index = chr(ord(index) + 1)
