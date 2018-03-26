from Rules import Rules

rules = Rules('rules.txt')

print rules.get_definitions()
print rules.get_expressions()
print rules.get_keywords()
print rules.get_punctuations()