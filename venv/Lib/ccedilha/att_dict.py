from att import Att


class AttDict:
    def __init__(self):
        self.dictionary = {}

    def insert(self, att_name: str, value, t: type):
        if not self.check_exist(att_name, t):
            self.dictionary[att_name] = Att(value, t)        

    def getValue(self, att_name, t: type):
        if self.check_exist(att_name, t):
            return self.dictionary[att_name].getValue(t)
    
    def setValue(self, att_name, value):
        self.dictionary[att_name] = value;

    def check_exist(self, att_name: str, t: type):
        if att_name in self.dictionary:
            if self.dictionary[att_name].getType() == t or t == None:          
                return True
        return False