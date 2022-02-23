class RuleCondition:
    def prepare_from_expression(self):
       tokens = self.expression.split(" ")
       self.right = tokens[0]
       self.operator = tokens[1]
       if (tokens[1] == "="):
            self.operator = "EQ"
       elif (tokens[1] == ">"):
            self.operator = "GT"
       elif (tokens[1] == "<"):
            self.operator = "LT"
       self.left = tokens[2]
       
    def __init__(self,right=None, operator=None, left=None , 
                  expression=None, andconditions=None, orconditions=None):
       self.expression = expression
       self.left = left
       self.right = right
       self.operator = operator
       self.variables = None
       if (expression != None) :
          self.prepare_from_expression()
       self.andconditions = andconditions
       self.orconditions = orconditions
       if (self.andconditions != None):
          self.operator = "AND"
       if (self.orconditions != None):
          self.operator = "OR"
          
    
    def to_string(self):
       if (self.operator == "AND"):
          _str = "and ["
          for condition in self.andconditions :
            _str = _str + condition.to_string()+", " 
          _str = _str+"] "
          return _str
       else:
         return str(self.right)+" "+self.operator+" "+str(self.left) 

    
