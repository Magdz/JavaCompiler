
class State(object):
	def __init__(self, name):
		self.epsilon = []
		self.transitions = {}
		self.name = name
		self.is_end = False
		self.key = True