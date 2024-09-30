class Character:

    def __init__(self, name="", hp=100, attack=10):
        self.name = name
        self.hp = hp
        self.maxhp = self.hp
        self.attack = attack

    def get_name(self) -> str:
        return self.name

    def get_hp(self) -> int:
        return self.hp

    def get_maxhp(self) -> int:
        return self.maxhp

    def get_attack(self) -> int:
        return self.attack

    def is_dead(self) -> bool:
        return self.hp <= 0

    def change_hp(self, change: int) -> None:
        self.hp += change
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def increase_hp(self, change: int) -> None:
        # changes hp but also changes max_hp
        self.hp += change
        self.maxhp += change

    def change_attack(self, change: int) -> None:
        self.attack += change
