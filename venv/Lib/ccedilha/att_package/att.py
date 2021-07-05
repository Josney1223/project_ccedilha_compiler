
class Att:
    def __init__(self, value, t: type, isList: bool, size: int):
        self.isList = isList  
        self.type = t      
        if self.isList is True:
            self.value = []            
            for i in range(size):
                self.value.append(None)
        else:
            self.value = value        

    def getValue(self, t: type):
        if self.type == t or t == "wildcard":
            return self.value
        else:
            raise Exception("TypeError: Tipo inválido ao pegar valor da variavel")

    def getType(self):
        return self.type

    def setValue(self, value, t: type):
        if self.type == t and not self.isList:
            self.value = value
        else:
            raise TypeError
        
    def insertList(self, index: int, value, t: type):
        if self.isList and self.type == t:
            self.value[index] = value
        else:
            raise TypeError