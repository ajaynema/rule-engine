class Telemetry:
    def __init__(self, data):
       self.data = data
    
    def add(self, key , value) :
        self.data[key] = value
    
    def get(self, key) :
        return self.data[key] 
