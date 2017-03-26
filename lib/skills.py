


class BaseSkill:
    def __init__(self):
        self.effects = {
            'health': 0,
            'attack': 0,
            'defense': 0,
            'mana': 0
        }
        self.name = ''

    def use(self):
        return self.effects

class StrongAttack(BaseSkill):
    def __init__(self):
        BaseSkill.__init__(self)
        self.effects['mana'] = 2
        self.effects['attack'] = 30
        self.name = 'strong attack'
