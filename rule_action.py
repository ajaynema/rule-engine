class RuleAction:
    def __init__(self, action=None, data=None):
       self.action = action
       self.data  = data
    
    def getData(self):
        return self.data

    def to_string(self):
        return "action="+self.action + ", data="+self.data.to_string()
       
