from base_action_handler import BaseHandler

class SendEmailHandler (BaseHandler):
    def __init__(self):
        super().__init__("SEND_EMAIL")
        
    def process(self, rule =None , action=None,telemetry=None):
        print("Sending Email")
        print(action.to_string())