class Character:
    def __init__(self, name = "", hp = 100, attack = 10):
        self.name = name
        self.hp = hp
        self.maxhp = self.hp
        self.attack = attack

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def change_hp(self,change):
        self.hp += change
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def increase_hp(self,change):
        # changes hp but also changes max_hp
        self.hp += change
        self.maxhp += change

    def change_attack(self,change):
        self.attack += change