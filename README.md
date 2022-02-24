# Rule-engine
Rule Engine for applying the rules on data stream.

Usage :

Step 1 : Define the template in json.
Step 2 : Register the template with rule engine
Step 3 : Define rule using template
Step 4 : Register rule with rule engine
Step 5 : Implement action handler
Step 6 : Register handler with Rule Engine
Step 7 : Now Rule engine ready to apply rule give data to rule engine 

Example
Templete :
    { 
        "name" : "alarm_rule_template",
        "scope" : {
                "deviceType" : "{{rule.deviceType}}"
        },
        "condition" : { 
             "expression" :  "{{telemetry.messageId}} = {{rule.messageId}}"
        },
        "action" : {
            "action" :  "SEND_EMAIL"
        }
    }

Rule :
    {
        "name" : "pitlid_301_rule",
        "template" :"alarm_rule_template",
        "variables" : {
            "messageId" : "301",
            "deviceType": "pitlid"
        }
}


Use in Script :

# Loading Rules and Temlete and register with the Rule Engine
def initialize(rule_engine):
    # Template Json
    json = { "name" : "alarm_rule_template","scope" : {"deviceType" : "{{rule.deviceType}}"},"condition" : { "expression" :  "{{telemetry.messageId}} = {{rule.messageId}}"},"action" : {"action" :  "SEND_EMAIL"}}
    
# create template from json
    rule_template = RuleTemplate(json_template=json)
    
# register/add template with rule engine
    rule_engine.add_template(rule_template)
    
# Rule Json
    json_rule_301 ={"name" : "pitlid_301_rule","template" :"alarm_rule_template","variables" : {"messageId" : "301","deviceType": "pitlid"}}
    
# create rule with json
    rule_301 = Rule(json_rule=json_rule_301)
    
# Register/add Rule with Rule Engine
    rule_engine.add_rule(rule_301)

# register Hnadlers
    rule_engine.add_handler(ReportAlarmHandler())
    rule_engine.add_handler(SendEmailHandler())    

# Test case Pass the telemetry data
def test(rule_engine):
    print("===== Start Test case 1======")
    telemetry = TelemetryData()
    telemetry.add("deviceType", "pitlid")
    telemetry.add("messageId", "301")
    rule_engine.process(telemetry)
    print("===== End ======\n\n")

# Main Class for calling test
def main():
     rule_engine = RuleEngine()    
     initialize(rule_engine)
     test(rule_engine)

if __name__=="__main__":
    main()
