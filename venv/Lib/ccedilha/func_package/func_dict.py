from func_package.func import func

class funcDict():
    def __init__(self):
        self.functions = {}
        
    def insertFunction(self, func_name: str, t: type, args: list, tree):
        if not self.check_exist(func_name):
            self.functions[func_name] = func(args, t, tree)
            
    def call_function(self, func_name: str, args: list):
        if self.check_exist(func_name):
            return self.functions[func_name].get_tree(args)
        else:
            raise Exception
        
    def get_args(self, func_name: str):
        if self.check_exist(func_name):
            return self.functions[func_name].get_args()
        
    def check_exist(self, func_name: str):
        if func_name in self.functions:          
            return True
        return False
    
    def print_func_list(self):
        print(self.functions)