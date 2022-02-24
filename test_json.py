from rule_condition import RuleCondition
from rule_action import RuleAction
from rule_template import RuleTemplate
from rule_engine import RuleEngine
from rule import Rule
from rule_data import RuleData
from rule_scope import RuleScope
from telemetry_data import TelemetryData
from action_handler_send_email import SendEmailHandler
from action_handler_report_alarm import ReportAlarmHandler


def initialize(rule_engine):
    json = { "name" : "alarm_rule_template","scope" : {"deviceType" : "{{rule.deviceType}}"},"condition" : { "expression" :  "{{telemetry.messageId}} = {{rule.messageId}}"},"action" : {"action" :  "SEND_EMAIL"}}
    rule_template = RuleTemplate(json_template=json)
    rule_engine.add_template(rule_template)
    json_rule_301 ={"name" : "pitlid_301_rule","template" :"alarm_rule_template","variables" : {"messageId" : "301","deviceType": "pitlid"}}
    rule_301 = Rule(json_rule=json_rule_301)
    rule_engine.add_rule(rule_301)

    rule_engine.add_handler(ReportAlarmHandler())
    rule_engine.add_handler(SendEmailHandler())    

def test1(rule_engine):
    print("===== Start Test case 1======")
    telemetry = TelemetryData()
    telemetry.add("deviceType", "pitlid")
    telemetry.add("messageId", "301")
    rule_engine.process(telemetry)
    print("===== End ======\n\n")

def main():
     rule_engine = RuleEngine()    
     initialize(rule_engine)
     test1(rule_engine)
   #  test2(rule_engine)
    # test3(rule_engine)
     
if __name__=="__main__":
    main()