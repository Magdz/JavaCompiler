from State import State
import string

class DFA(object):
    def __init__(self, nfa):
        self.nfa = nfa
        self.state_index = 0
        self.symbols = []
        self.start_e_closure = self.e_closure(self.nfa.start)
        print(self.symbols)

        self.convert_NFA_to_DFA()

    def e_closure(self, state):
        e_closure_state = self.create_state()
        self.e_closure_states(state, e_closure_state)
        # Epsilon(0) always contains itself
        e_closure_state.nfa_corresponding_states.append(state)
        return e_closure_state

    def e_closure_states(self, state, e_closure):
        if not state.epsilon:
            self.symbols.append(state.transitions.keys()[0])
            return
        for eps_state in state.epsilon:
            self.e_closure_states(eps_state, e_closure)
            e_closure.nfa_corresponding_states.append(eps_state)

    def state_index_ascii(self, state_index):
        return list(string.ascii_uppercase)[state_index]

    def create_state(self):
        state = State(self.state_index_ascii(self.state_index))
        self.state_index += 1
        return state

    def convert_NFA_to_DFA(self):
        DFA_stack = []
        # Push initial state to DFA_stack
        DFA_stack.append(self.start_e_closure)
        # Evaluate the stack
        self.build_DTrans(DFA_stack)

    def build_DTrans(self, DFA_stack):
        if len(DFA_stack) == 0:
            return
        dfa_state = DFA_stack.pop()
        for symbol in self.symbols:
            self.evaluate_symbol_on_state(symbol, dfa_state, DFA_stack)
        self.build_DTrans(DFA_stack)

    def evaluate_symbol_on_state(self, symbol, dfa_state, stack):
        nfa_states = dfa_state.nfa_corresponding_states
        new_dfa_state = self.create_state()
        self.build_new_dfa_state(nfa_states, symbol, new_dfa_state)
        exists = None
        for item in stack:
            if item.nfa_corresponding_states == new_dfa_state.nfa_corresponding_states:
                exists = item
        if not exists:
            stack.append(new_dfa_state)
        else:
            new_dfa_state = exists
        dfa_state.dfa_state_transitions.append(new_dfa_state)


    def build_new_dfa_state(self, nfa_states, symbol, new_dfa_state):
        if nfa_states.count == 0:
            return
        for nfa_state in nfa_states:
            for trans_symbol in nfa_state.transitions:
                if symbol == trans_symbol:
                    if nfa_state.transitions[trans_symbol] not in new_dfa_state.nfa_corresponding_states:
                        new_dfa_state.nfa_corresponding_states.append(nfa_state.transitions[trans_symbol])
                    self.build_new_dfa_state(nfa_state.transitions[trans_symbol].epsilon, symbol, new_dfa_state )
            for eps_state in nfa_state.epsilon:
                new_dfa_state.nfa_corresponding_states.append(eps_state)
                self.build_new_dfa_state(eps_state.epsilon, symbol, new_dfa_state)
