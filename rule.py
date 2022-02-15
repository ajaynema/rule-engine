import copy

class Rule:
    def replace_variables(self, condition):
        if (condition.operator == "AND"):
            for cond in condition.andconditions:
                self.replace_variables(cond)
        elif (condition.operator == "OR"):
            for cond in condition.orconditions:
                self.replace_variables(cond)
        else:
            if (condition.left.startswith("{{")):
                variable = condition.left.replace("{{","")
                variable = variable.replace("}}","")
                print("variable="+variable)
                value = self.variables.get(variable)
                condition.left = value
                print("value="+str(value))
                print(condition.to_string())
       
    def prepare(self):
        self.condition = self.template.condition
        self.action = self.template.action
        self.scope = self.template.scope
        self.replace_variables(self.condition)
        print("Rule Prepare : " + self.condition.to_string())
    
    def to_string(self):
        print("condition=" + self.condition.to_string()+"action="+action.to_string())
            
    def __init__(self,name, template, variables):
       self.name = name
       self.template = copy.deepcopy(template)
       self.variables = variables
       self.prepare()
       self.andrules = None
    
    

       