
class Rules(object):

	def __init__(self, filename):
		self.__definitions = {}
		self.__expressions = {}
		self.__keywords = []
		self.__punctuations = []
		self.__import(filename)

	def __import(self, filename):
		with open(filename, 'r') as file:
			for line in file:
				prev_char = None
				for char in line:
					if(char == '=' and not prev_char == '\\'):
						kv = line.split('=')
						self.__definitions[kv[0].strip(' \t\n\r')] = kv[1].strip(' \t\n\r')
					if(char == ':' and not prev_char == '\\'):
						kv = line.split(':')
						kv[1] = kv[1].replace('\\', '')
						self.__expressions[kv[0].strip(' \t\n\r')] = kv[1].strip(' \t\n\r')
					if(char == '{' and prev_char == None):
						keywords = line.split(' ')
						for keyword in keywords:
							keyword = keyword.strip('{\}\n')
							self.__keywords.append(keyword)
					if(char == '[' and prev_char == None):
						punctuations = line.split(' ')
						for punctuation in punctuations:
							punctuation = punctuation.strip('[]\n\\')
							self.__punctuations.append(punctuation)
					prev_char = char

	def get_definitions(self):
		return self.__definitions

	def get_expressions(self):
		return self.__expressions

	def get_keywords(self):
		return self.__keywords

	def get_punctuations(self):
		return self.__punctuations
