from NFA import NFA
from State import State

class Handler(object):
	def __init__(self):
		self.handlers = {'SYMBOL': self.handle_symbol,
						 'CONCAT': self.handle_concat,
						 'ALT': self.handle_alt,
						 'STAR': self.handle_rep,
						 'PLUS': self.handle_rep,
						}
		self.state_count = 0

	def create_state(self):
		self.state_count += 1
		return State('s' + str(self.state_count))

	def handle_symbol(self, token, nfa_stack):
		s0 = self.create_state()
		s1 = self.create_state()
		s0.transitions[token.value] = s1
		nfa = NFA(s0, s1)
		nfa_stack.append(nfa)

	def handle_concat(self, token, nfa_stack):
		nfa2 = nfa_stack.pop()
		nfa1 = nfa_stack.pop()
		nfa1.end.is_end = False
		nfa1.end.epsilon.append(nfa2.start)
		nfa = NFA(nfa1.start, nfa2.end)
		nfa_stack.append(nfa)

	def handle_alt(self, token, nfa_stack):
		nfa2 = nfa_stack.pop()
		nfa1 = nfa_stack.pop()
		s0 = self.create_state()
		s0.epsilon = [nfa1.start, nfa2.start]
		s1 = self.create_state()
		nfa1.end.epsilon.append(s1)
		nfa2.end.epsilon.append(s1)
		nfa1.end.is_end = False
		nfa2.end.is_end = False
		nfa = NFA(s0, s1)
		nfa_stack.append(nfa)

	def handle_rep(self, token, nfa_stack):
		nfa1 = nfa_stack.pop()
		s0 = self.create_state()
		s1 = self.create_state()
		s0.epsilon = [nfa1.start]
		if token.name == 'STAR':
			s0.epsilon.append(s1)
		nfa1.end.epsilon.extend([s1, nfa1.start])
		nfa1.end.is_end = False
		nfa = NFA(s0, s1)
		nfa_stack.append(nfa)
