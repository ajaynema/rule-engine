import json
from rule_data import RuleData
from rule_action import RuleAction
from rule_condition import RuleCondition
from rule_variable import RuleVariable
class RuleTemplate:

    def load_from_json(self, json_template):
        self.name = json_template.get("name")
        json_scope = json_template.get('scope')
        self.scope = RuleData()
        for key in json_scope:
            self.scope.add(key,json_scope.get(key))
        json_action = json_template.get('action')
        self.action = RuleAction(json_action.get('action'))
        json_condition =  json_template.get('condition')
        json_expression = json_condition.get('expression')
        self.condition = RuleCondition(expression = json_expression)
        json_variable_metedata = json_template.get('variable_metadata')
        self.variable_metedata = {}
        for json_variable in json_variable_metedata :
            variable = RuleVariable(json_variable.get("name"))
            variable.set_type(json_variable.get("type"))
            variable.set_default_value(json_variable.get("default_value"))
            self.variables[variable.get_name()] = variable


    def __init__(self, name=None, scope=None, condition=None, action=None, variables=None, json_template=None):
       self.name = name
       self.scope = scope
       self.condition = condition
       self.action = action
       self.json_template = json_template
       self.variables = variables
       if (json_template != None):
        self.load_from_json(json_template)
    
    def get_name(self):
        return self.name

    