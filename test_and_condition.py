from condition import Condition
from action import Action
from rule_template import RuleTemplate
from rule_engine import RuleEngine
from rule import Rule
from data import Data
from scope import Scope


def initialize(rule_engine):
    andconditions = [
            Condition(expression="{{telemetry.temperature}} > {{temperature_threshold}}"),
            Condition(expression="{{telemetry.humidity}} > {{humidity_threshold}}")]
    condition = Condition(andconditions=andconditions)
    action = Action("DISPLAY", {})
    
    scope = Scope()
    scope.add("season","SUMMER")
    rule_template = RuleTemplate(scope=scope, condition=condition, action=action)
    data = Data()
    data.add("temperature_threshold",98)
    data.add("humidity_threshold",50)
    rule = Rule("Rule-Summer-Weather-rule",rule_template, data)
    rule_engine.addRule(rule)  

    action = Action("PRINT", {})
    scope = Scope()
    scope.add("season","WINTER")
    rule_template = RuleTemplate(scope=scope, condition=condition, action=action)
    data = Data()
    data.add("temperature_threshold",70)
    data.add("humidity_threshold",50)
    rule = Rule("Rule-Winter-Weather-rule",rule_template, data)
    rule_engine.addRule(rule)  
    

def test1(rule_engine):
    print("===== Start Test case 1======")
    telemetry = Data()
    telemetry.add("season", "WINTER")
    telemetry.add("temperature", 60)
    telemetry.add("humidity", 60)
    rule_engine.process(telemetry)
    print("===== End ======\n\n")

def test2(rule_engine):
    print("===== Start Test case 2======")
    telemetry = Data()
    telemetry.add("season", "WINTER")
    telemetry.add("temperature", 80)
    telemetry.add("humidity", 60)
    rule_engine.process(telemetry)
    print("===== End ======\n\n")

def test3(rule_engine):   
    print("===== Start test case 3 ======")
    telemetry = Data()
    telemetry.add("season", "SUMMER")
    telemetry.add("temperature", 100)
    telemetry.add("humidity", 70)
    rule_engine.process(telemetry)
    print("===== End ======\n\n")
    

def main():
     rule_engine = RuleEngine()    
     initialize(rule_engine)
     test1(rule_engine)
     test2(rule_engine)
     test3(rule_engine)
     

if __name__=="__main__":
    main()