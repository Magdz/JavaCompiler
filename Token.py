
class Token(object):
	def __init__(self, name, value):
		self.name = name
		self.value = value.replace('\\', '')

	def __str__(self):
		return self.name + ":" + self.value
		