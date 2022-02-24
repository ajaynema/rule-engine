import copy
from rule_data import RuleData
class Rule:
    def load_from_json(self, json_rule):
        self.name = json_rule.get("name")
        self.template_name =  json_rule.get("template")
        json_variables = json_rule.get('variables')
        self.variables = RuleData()
        for key in json_variables:
            self.variables.add(key,json_variables.get(key))
               
    def get_name(self):
        return self.name

    def get_template_name(self):
        return self.template_name

    def set_template(self,template):
        self.template = copy.deepcopy(template)
        self.prepare()        
    
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
                variable = variable.replace("rule.","")
                print("variable="+variable)
                value = self.variables.get(variable)
                condition.left = value
                print("value="+str(value))
                print(condition.to_string())
        if (self.scope != None):
                for key in self.scope.getData():
                    scope_value = self.scope.get(key)
                    if (scope_value.startswith("{{")):
                         variable = scope_value.replace("{{","")
                         variable = variable.replace("}}","")
                         variable = variable.replace("rule.","")
                         value = self.variables.get(variable)
                         self.scope.set(variable, value)


    def prepare(self):
        self.condition = self.template.condition
        self.action = self.template.action
        self.scope = self.template.scope
        self.variable_mete_data = self.template.variable_metadata
        self.replace_variables(self.condition)
        print("Rule Prepare : " + self.condition.to_string())
    
    def to_string(self):
        print("condition=" + self.condition.to_string()+"action="+self.action.to_string())
            
    def __init__(self,name=None, template=None, variables=None, json_rule=None):
       self.name = name
       self.scope = None
       self.template_name = None
       self.template = None
       self.andrules = None
       self.variables = None
       
       if (json_rule != None) :
           self.load_from_json(json_rule)
       else:
            self.template = copy.deepcopy(template)
            self.variables = variables
            self.andrules = None
            self.prepare()
    