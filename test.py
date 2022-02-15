from condition import Condition
from action import Action
from rule_template import RuleTemplate
from rule_engine import RuleEngine
from rule import Rule
from telemetry import Telemetry


def initialize(rule_engine):
    condition = Condition("a" , "EQ", "{{value}}")
    action = Action("DISPLAY", {})
    rule_template = RuleTemplate(condition=condition, action=action)
    rule = Rule("Rule-1",rule_template, None)
    rule_engine.addRule(rule)  

def test1(rule_engine):
    telemetry = Telemetry()
    telemetry.add("value", 6)
    rule_engine.process(telemetry)
    

def main():
     rule_engine = RuleEngine()    
     initialize(rule_engine)
     test1(rule_engine)

if __name__=="__main__":
    main()