from base_action_handler import BaseHandler

class ReportAlarmHandler (BaseHandler):
    def __init__(self):
        super().__init__("REPORT_ALARM")
        
    def process(self, rule =None , action=None, telemetry=None):
        print("Report Alarm")