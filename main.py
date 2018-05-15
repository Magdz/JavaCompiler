from Lexical import Lexical
from Parser import Parser   

lexical = Lexical('rules.txt')
tokens = lexical.analize('code.txt')
tokens = ['int', 'id', ';', 'id', 'assign', 'num', ';', 'if', '(', 'id', 'relop', 'num', ')',
 '{', 'id', 'assign', 'num', ';', '}'] 
print tokens
parser = Parser('grammar.txt')
tree = parser.analyze(tokens)
for item in tree:
    print item