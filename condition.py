class Condition:
    def __init__(self,left=None, operator=None, right=None , expression=None):
       self.expression = expression
       self.left = left
       self.right = right
       self.operator = operator
       self.variables = None
    
