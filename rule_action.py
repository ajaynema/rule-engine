class RuleAction:
    def __init__(self, action , data=None):
       self.action = action
       self.data  = data
    
    def to_string(self):
        return self.action
       
