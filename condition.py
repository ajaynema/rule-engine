class Condition:
    def __init__(self,right=None, operator=None, left=None , expression=None):
       self.expression = expression
       self.left = left
       self.right = right
       self.operator = operator
       self.variables = None
    
    def to_string(self):
       return str(self.right)+" "+self.operator+" "+str(self.left) 
    
