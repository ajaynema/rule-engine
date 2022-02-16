import copy
import json
import jsonpickle
from action_handler_report_alarm import ReportAlarmHandler
from action_handler_send_email import SendEmailHandler


class RuleEngine:
    def __init__(self):
        self.rules = []
        self.handlers = {}
    
    def add_rule(self, rule):
        self.rules.append(rule) 
    
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
            return false    
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
        handler = self.handlers[rule.action.action]
        if (handler != None):
            handler.process(rule,telemetry)
        elif (rule.action.action == "DISPLAY"):
            self.do_display(rule,telemetry)
        elif(rule.action.action == "PRINT"): 
            self.do_print(rule,telemetry)  
       

    def process(self, telemetry):
        matching_rules =  self.get_matching_rules(telemetry)
        if (len(matching_rules) > 0):
            print("found " + str(len(matching_rules)) + " maching rules rules")
            for rule  in matching_rules:
                print("Rule="+rule.name)
                self.do_action(rule,telemetry)
        else:
            print("no matching rule found ")
  
    
