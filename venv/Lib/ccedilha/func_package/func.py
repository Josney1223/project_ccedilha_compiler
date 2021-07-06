
class func():
    def __init__(self, args: list, t: type, tree):
        self.args = args
        self.t = t
        self.tree = tree
    
    def get_tree(self, args: list):
        if len(args) == len(self.args) or args == "wildcard":
            return self.tree
        else:
            raise Exception
        
    def get_args(self):
        return self.args