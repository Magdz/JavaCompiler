
class Rules(object):

    def __init__(self, filename):
    	self.__expressions = {}
    	self.__definitions = {}
    	self.__keywords = []
    	self.__import(filename)

    def __import(self, filename):
        with open(filename, 'r') as file:
        	for line in file:
        		prev_char = None
        		for char in line:
        			if(char == '=' and not prev_char == '\\'):
	        			kv = line.split('=')
	        			self.__expressions[kv[0].strip(' \t\n\r')] = kv[1].strip(' \t\n\r')
	        		if(char == ':' and not prev_char == '\\'):
	        			kv = line.split(':')
	        			self.__definitions[kv[0].strip(' \t\n\r')] = kv[1].strip(' \t\n\r')
        			if(char == '{' and prev_char == None):
        				keywords = line.split(' ')
        				print keywords
        			prev_char = char

		print self.__expressions
		print self.__definitions
		print self.__keywords

