# from CFG import CFG

class Parser(object):
    def __init__(self, grammarFile):
        self.tree = []
        # cfg = CFG(grammarFile)
        # self.cfg = cfg.get_grammar()
        self.cfg = {
            'METHOD_BODY': [['LIST']],
            'LIST': [['STAT'], ['LIST', 'STAT']],
            'STAT': [['DECLA'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
            'DECLA': [['PRI_TYPE', 'id', ';']],
            'PRI_TYPE': [['int'], ['float']],
            'IF': [['if', '(', 'EXP', ')', '{', 'STAT', '}']],
            'WHILE': [['while', '(', 'EXP', ')', '{', 'STAT', '}']],
            'ASSIGNMENT': [['id', 'assign', 'EXP', ';']],
            'EXP': [['SIM'], ['SIM', 'relop', 'SIM']],
            'SIM': [['TERM'], ['SIGN', 'TERM'], ['SIM', 'addop', 'TERM']],
            'TERM': [['FACTOR'], ['TERM', 'mulop', 'FACTOR']],
            'FACTOR': [['id'], ['num'], ['(', 'EXP', ')']],
            'SIGN': [['+'], ['-']]
        }
        pass

    def analyze(self, tokens):
        self.tokens = tokens
        start_stage = ['METHOD_BODY']
        self.__analyze(start_stage)
        self.tree.insert(0, start_stage)
        return self.tree

    def __analyze(self, stage):
        print stage
        if stage == ['STAT', 'STAT', 'STAT']:
            print stage
        if len(stage) > len(self.tokens):
            return
        if stage == self.tokens:
            return stage
        for index, key in enumerate(stage):
            if key in self.cfg:
                for case in self.cfg[key]:
                    new_stage = self.__replace(stage, index, case)
                    next_stage = self.__analyze(new_stage)
                    if next_stage != None:
                        self.tree.insert(0, next_stage)
                        return stage


    def __replace(self, stage, index, values):
        stage = list(stage)
        del stage[index]
        for value in values:
            stage.insert(index, value)
            index += 1
        return stage
