from Lexical import Lexical

lexical = Lexical('rules.txt', 'code.txt')

# nfa_test = nfa_dict['num']
print lexical.nfa.match(['digit', 'digit'])
