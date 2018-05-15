from Lexical import Lexical
<<<<<<< HEAD
from Parser import Parser   

lexical = Lexical('rules.txt')
tokens = lexical.analize('code.txt')
tokens = ['int', 'id', ';', 'id', 'assign', 'num', ';'] 
print tokens
parser = Parser('grammar.txt')
tree = parser.analyze(tokens)
for item in tree:
    print item
=======
from CFG import CFG
# lexical = Lexical('rules.txt')
# tokens = lexical.analize('code.txt')
# print tokens
CFG('grammar.txt')
>>>>>>> 613813030fa9470a48070fb5308fbb79e4bfeb42
