import json
import jsonpickle

class RuleData (object):
    
    def __init__(self):
        self.data = {}

    def add(self, key , value) :
        self.data[key] = value
    
    def get(self, key) :
        return self.data[key] 
    
    def set(self, key,value) :
        self.data[key] = value
   
    def getData(self):
        return self.data
    
    def to_string(self):
        return json.dumps(json.loads(jsonpickle.encode(self.data)), indent=2)
