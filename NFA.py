
class NFA(object):

	def __init__(self, start, end):
		self.start = start
		self.end = end
		end.is_end = True
