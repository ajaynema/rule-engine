class RuleTemplateFactory:
    def __init__(self):
       self.templates = []
    
    def register(self, template):
       self.templates[template.name] = template

    def get(self, name):
       return self.templates[name]
