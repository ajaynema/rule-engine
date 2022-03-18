import copy
import json
from re import template
import jsonpickle
from action_handler_report_alarm import ReportAlarmHandler
from action_handler_send_email import SendEmailHandler


class RuleEngine:
    def __init__(self):
        self.rules = []
        self.handlers = {}
        self.templates = {}
    
    def prepare_action(self, rule = None,action = None,telemetry = None):
        for key in action.getData().getData():
            data_value = action.getData().get(key)
            if (data_value.startswith("{{")):
                    variable = data_value.replace("{{","")
                    variable = variable.replace("}}","")
                    variable = variable.replace("telemetry.","")
                    value = telemetry.get(variable)
                    action.getData().set(variable, value)

    def add_rule(self, rule):
        if rule.get_template_name() != None:
            template = self.get_template(rule.get_template_name())
            rule.set_template(template)
        self.rules.append(rule) 
    
    def add_template(self, template):
        self.templates[template.get_name()] =  template
    
    def get_template(self, template_name):
        return self.templates[template_name]
    
    def add_handler(self, handler):
        name = handler.get_name()
        self.handlers[name] = handler

    def get_handler(self, action):
        return self.handlers[action]
    
    def prepare(self,condition,telemetry):
        if (condition.operator == "EQ" or condition.operator == "GT"  or condition.operator == "LT" ):
           if (condition.right.startswith("{{")):
                variable = condition.right.replace("{{","")
                variable = variable.replace("}}","")
                variable = variable.replace("telemetry.","")
                #print ("variable = "+variable)
                value = telemetry.get(variable)
                condition.right = value
        elif (condition.operator == "AND"):
            for condition in condition.andconditions:
                self.prepare(condition,telemetry)
        elif (condition.operator == "OR"):
            for condition in condition.orconditions:
                self.prepare(condition,telemetry)
    
    def eval(self,condition):
        if (condition.operator == "EQ"):
            if (condition.right == condition.left):
                return True
        elif (condition.operator == "GT"):
                if (condition.right > int(condition.left)):
                    return True 
        elif (condition.operator == "LT"):
                if (condition.right < condition.left):
                    return True 
        elif (condition.operator == "AND"):
            for  cond in condition.andconditions:
                if (self.eval(cond) != True):
                    return False
            return True   
        elif (condition.operator == "OR"):
            for cond in condition.orconditions:
                if (self.eval(cond)):
                    return True
            return False    
        return False

       
    def match_scope(self, rule, telemetry):
        for key in rule.scope.getData():
            #print("scope : key=" +key+", scope value=" + rule.scope.get(key)+",telemetry value=" + telemetry.get(key))
            if (rule.scope.get(key) != telemetry.get(key)):
                    return False
        return True

    def get_matching_rules(self, telemetry):
        print("processing : " + json.dumps(json.loads(jsonpickle.encode(telemetry)), indent=2))
        maching_rules = []
        for rule in self.rules:
           copy_rule = copy.deepcopy(rule) 
           if (self.match_scope(copy_rule,telemetry)):
                self.prepare(copy_rule.condition,telemetry)
                if (self.eval(copy_rule.condition)):
                        maching_rules.append(rule)
        return maching_rules
    
    def do_display(self,rule,telemetry):
        print("Action=DISPLAY")
    
    def do_print(self,rule,telemetry):
        print("Action=PRINT")

    def do_action(self,rule,telemetry):
        if (rule.action != None):
            handler = self.handlers[rule.action.action]
            if (handler != None):
                self.prepare_action(rule=rule, action=rule.action,telemetry=telemetry)
                handler.process(rule=rule,telemetry=telemetry,action=rule.action)
            elif (rule.action.action == "DISPLAY"):
                self.do_display(rule,telemetry)
            elif(rule.action.action == "PRINT"): 
                self.do_print(rule,telemetry)  
        if (rule.actions != None):
            for action in self.actions:
                handler = self.handlers[action.action]
                if (handler != None):
                    self.prepare_action(rule=rule,action=action,telemetry=telemetry)
                    handler.process(rule=rule,telemetry=telemetry,action=action)
                    
            
        

    def process(self, telemetry):
        matching_rules =  self.get_matching_rules(telemetry)
        if (len(matching_rules) > 0):
            print("found " + str(len(matching_rules)) + " maching rules rules")
            for rule  in matching_rules:
                print("Rule="+rule.name)
                self.do_action(rule,telemetry)
        else:
            print("no matching rule found ")
  
    
