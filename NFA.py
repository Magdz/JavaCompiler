
class NFA(object):

	def __init__(self, start, end):
		self.start = start
		self.end = end
		end.is_end = True

	def add_state(self, state, states_set):
		if state in states_set:
			return
		states_set.add(state)
		for eps in state.epsilon:
			self.add_state(eps, states_set)

	def match(self, string):
		current_states = set()
		self.add_state(self.start, current_states)
		for char in string:
			next_states = set()
			for state in current_states:
				if char in state.transitions.keys():
					transition_state = state.transitions[char]
					self.add_state(transition_state, next_states)
			current_states = next_states
		for state in current_states:
			if state.is_end:
				return state.key
		return False

