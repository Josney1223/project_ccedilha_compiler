from att_package import att


class AttDict:
    def __init__(self):
        self.dictionary = {}

    def insert(self, att_name: str, value, t: type, isList: bool, size: int):
        if not self.check_exist(att_name, "wildcard"):
            self.dictionary[att_name] = att.Att(value, t, isList, size)        

    def getValue(self, att_name, t: type):
        if self.check_exist(att_name, t):
            return self.dictionary[att_name].getValue(t)
        else:
            self.show_all()
            raise Exception("Tipo inválido ou variavel "+att_name+" inexistente")
    
    def setValue(self, att_name, value, t: type):
        if self.check_exist(att_name, t):
            self.dictionary[att_name].setValue(value, t)
        else: 
            raise TypeError
    
    def insertList(self, att_name: str, index: int, value, t: type):
        if self.check_exist(att_name, t):
            self.dictionary[att_name].insertList(index, value, t)
        else: 
            raise TypeError        

    def check_exist(self, att_name: str, t: type):
        if att_name in self.dictionary:
            if self.dictionary[att_name].getType() == t or t == "wildcard":          
                return True
        return False
    
    def show_all(self):
        for keys, values in self.dictionary.items():
            print(keys, values.getValue("wildcard"), values.getType())