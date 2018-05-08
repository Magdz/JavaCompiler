from DFA import DFA
from Lexical import Lexical

lexical = Lexical('rules.txt')
tokens = lexical.analyse('code.txt')
lexical.print_nfa()
nfa = lexical.get_nfa()
dfa = DFA(nfa)
# print tokens
