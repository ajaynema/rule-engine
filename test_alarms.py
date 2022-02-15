from condition import Condition
from action import Action
from rule_template import RuleTemplate
from rule_engine import RuleEngine
from rule import Rule
from data import Data
from scope import Scope


def initialize(rule_engine):
    condition = Condition("{{telemetry.messageId}}" , "EQ", "{{rule.messageId}}")
    action = Action("REPORT_ALARM", {})
    
    
    scope = Scope()
    scope.add("device_type","PITLID")
    rule_template = RuleTemplate(scope=scope, condition=condition, action=action)
    data = Data()
    data.add("messageId",301)
    rule = Rule("301-message-rule",rule_template, data)
    rule_engine.addRule(rule)  

    action = Action("SEND_EMAIL", {})
    scope = Scope()
    scope.add("device_type","CAPTIS")
    rule_template = RuleTemplate(scope=scope, condition=condition, action=action)
    data = Data()
    data.add("messageId",201)
    rule = Rule("201-message-rule",rule_template, data)
    rule_engine.addRule(rule)  
    

def test1(rule_engine):
    print("===== Start Test case 1======")
    telemetry = Data()
    telemetry.add("device_type", "PITLID")
    telemetry.add("messageId", 201)
    rule_engine.process(telemetry)
    print("===== End ======\n\n")

def test2(rule_engine):
    print("===== Start Test case 2======")
    telemetry = Data()
    telemetry.add("device_type", "PITLID")
    telemetry.add("messageId", 301)
    rule_engine.process(telemetry)
    print("===== End ======\n\n")

def test3(rule_engine):   
    print("===== Start test case 3 ======")
    telemetry = Data()
    telemetry.add("device_type", "CAPTIS")
    telemetry.add("messageId", 301)
    rule_engine.process(telemetry)
    print("===== End ======\n\n")

def test4(rule_engine):   
    print("===== Start test case 4 ======")
    telemetry = Data()
    telemetry.add("device_type", "CAPTIS")
    telemetry.add("messageId", 201)
    rule_engine.process(telemetry)
    print("===== End ======\n\n")
    

def main():
     rule_engine = RuleEngine()    
     initialize(rule_engine)
     test1(rule_engine)
     test2(rule_engine)
     test3(rule_engine)
     test4(rule_engine)
     

if __name__=="__main__":
    main()