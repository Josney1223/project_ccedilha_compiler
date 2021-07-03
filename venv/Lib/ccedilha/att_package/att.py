
class Att:
    def __init__(self, value, t: type):
        self.value = value
        self.type = t

    def getValue(self, t: type):
        if self.type == t or t == "wildcard":
            return self.value
        else:
            raise Exception("TypeError: Tipo inválido ao pegar valor da variavel")

    def getType(self):
        return self.type

    def setValue(self, value, t: type):
        if self.type == t:
            self.value = value
        else:
            raise TypeError