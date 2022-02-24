class RuleVariable (object):
    def __init__(self, name, type="string",default_value=None):
        self.name = name
        self.type = type
        self.default_value = default_value 
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_default_value(self):
        return self.default_value

    def get_name(self):
        return self.name
    
    def set_type(self,type):
        self.type = type
    
    def set_default_value(self, default_value):
        self.default_value = default_value
    
    
