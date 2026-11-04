class Character:
    count = 0

    @classmethod
    def from_string(cls, data):
        name, hp = data.split(';')
        return cls(name, int(hp))

    @staticmethod
    def is_valid_name(name):
            if len(name) < 2 or len(name) > 20:
                return False
            else:
                return True
    
    def __eq__(self, other):
        return self.name == other.name and self.level == other.level
                

    def __init__ (self, name, hp=100, level=1):
        self.name = name
        self.hp = hp
        self.level = level
        self.max_hp = hp
        Character.count +=1
    
    def __str__(self):
        return f"{self.name} (Lv { self.level}, HP {self.hp})"

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
    
    @property
    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        target.take_damage(5)


class Warrior(Character):
    def __init__(self, name, hp=100, level=1, strength=10):
        super().__init__(name, hp, level)
        self.strength = strength
    def attack(self, target):
        target.take_damage(self.strength)

class Mage(Character):
    def __init__(self,name,hp=100,level=1, mana=50):
        super().__init__(name,hp,level)
        self.mana = mana

    def attack(self, target):
        if self.mana >=10:
            self.mana -=10
            target.take_damage(20)
        else:
            super().attack(target)
        
    def __str__(self):
        return f"{super().__str__()} MP {self.mana}"


class HealerMixin:
    def heal(self, target, amount):
        target.hp = min(target.max_hp, target.hp + amount)

class Priest(HealerMixin, Mage):
    pass

