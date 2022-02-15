class RuleTemplate:
    def __init__(self, scope, name, condition, action):
       self.name = name
       self.scope = scope
       self.condition = condition
       self.action = action