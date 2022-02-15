import copy
import json
import jsonpickle

class RuleEngine:
    def __init__(self):
        self.rules = []
    def addRule(self, rule):
        self.rules.append(rule) 
    def prepare(self,rule,telemetry):
         if (rule.condition.operator == "EQ" or rule.condition.operator == "GT"  or rule.condition.operator == "LT" ):
           if (rule.condition.right.startswith("{{")):
                variable = rule.condition.right.replace("{{","")
                variable = variable.replace("}}","")
                variable = variable.replace("telemetry.","")
                #print ("variable = "+variable)
                value = telemetry.get(variable)
                rule.condition.right = value    
    
    def eval(self,rule):
        if (rule.condition.operator == "EQ"):
            if (rule.condition.right == rule.condition.left):
                return True
        elif (rule.condition.operator == "GT"):
                if (rule.condition.right > rule.condition.left):
                    return True 
        elif (rule.condition.operator == "LT"):
                if (rule.condition.right < rule.condition.left):
                    return True    
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
                self.prepare(copy_rule,telemetry)
                if (self.eval(copy_rule)):
                        maching_rules.append(rule)
        return maching_rules
    
    def process(self, telemetry):
        matching_rules =  self.get_matching_rules(telemetry)
        if (len(matching_rules) > 0):
            print("found " + str(len(matching_rules)) + " maching rules rules")
            for rule  in matching_rules:
                print("Rule="+rule.name)
        else:
            print("no matching rule found ")
  
    
