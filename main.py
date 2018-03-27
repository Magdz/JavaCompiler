from Lexical import Lexical

lexical = Lexical('rules.txt')
tokens = lexical.analize('code.txt')
print tokens
