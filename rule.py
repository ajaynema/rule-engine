import copy

class Rule:
    def replace_variables(self):
       if (self.condition.operator == "EQ" or self.condition.operator == "GT" or self.condition.operator == "LT"):
           if (self.condition.left.startswith("{{")):
                variable = self.condition.left.replace("{{","")
                variable = variable.replace("}}","")
                value = self.variables.get(variable)
                self.condition.left = value
       
    def prepare(self):
        self.condition = self.template.condition
        self.action = self.template.action
        self.scope = self.template.scope
        self.replace_variables()
    
    def to_string(self):
        print("condition=" + self.condition.to_string())
            
    def __init__(self,name, template, variables):
       self.name = name
       self.template = copy.deepcopy(template)
       self.variables = variables
       self.prepare()
    
    

       