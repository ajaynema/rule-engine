class BaseHandler:
    def __init__(self, name=None):
        self.name = name
    
    def get_name(self):
        return self.name
        
    def process(self, rule =None , action=None):
        return "not implemented"