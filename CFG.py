import pprint

class CFG(object):
    def __init__(self, filename):
        self.__productions = {}
        self.__import(filename)
        self.print_productions()

    def __import(self, filename):
        RHS = []
        LHS = ''
        with open(filename, 'r') as file:
            for line in file:
                production = line.split('::=')
                if len(production) > 1:
                    if RHS: self.add_to_productions(LHS, RHS)
                    LHS = production[0]
                    RHS = production[1].split('|')
                else:
                    RHS.extend(production[0].split('|'))
                    continue
        self.add_to_productions(LHS, RHS)

    def add_to_productions(self, LHS, RHS):
        RHS = [item.split(' ') for item in RHS]
        RHS = self.clean(RHS)
        self.__productions[LHS.strip(' ')] = RHS

    def clean(self, RHS):
        NRHS = []
        for i, ORs in enumerate(RHS): 
            NORs = []
            for j, key in enumerate(ORs):
                key = key.rstrip()
                key = key.strip('\'')
                if key: 
                    NORs.append(key)
            if len(NORs) > 0:
                NRHS.append(NORs)
        return NRHS

    def print_productions(self):
        for x in self.__productions:
            print('\033[92m' + x + " :" + '\033[0m')
            print(self.__productions[x])

    def get_grammar(self):
        return self.__productions