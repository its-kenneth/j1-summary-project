class Move:
    def __init__(self, name: str, multiplier: float, power_limit: int):
        self.name = name
        self.multiplier = multiplier
        self.power_limit = power_limit
        self.current_power = power_limit
        
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_multiplier(self):
        return self.multiplier

    def set_multiplier(self, multiplier):
        self.multiplier = multiplier

    def get_power_limit(self):
        return self.power_limit

    def set_power_limit(self, power_limit):
        self.power_limit = power_limit

    def get_current_power(self):
        return self.current_power

    def used_moves(self):
        self.current_power -= 1
        if self.current_power == 0:
            return False
        else:
            return True 