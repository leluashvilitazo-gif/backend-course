def battle(a,b):
    while a.is_alive and b.is_alive:
        a.attack(b)
        if b.is_alive == False:
            return a
        else:
            b.attack(a)
        if a.is_alive == False:
            return b
        

def log_action(func):
    def wrapper(self, *args, **kwargs):
        print(f"{self.name} → {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

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

    @log_action
    def attack(self, target):
        target.take_damage(5)


class Warrior(Character):
    def __init__(self, name, hp=100, level=1, strength=10):
        super().__init__(name, hp, level)
        self.strength = strength
    @log_action
    def attack(self, target):
        target.take_damage(self.strength)

class Mage(Character):
    def __init__(self,name,hp=100,level=1, mana=50):
        super().__init__(name,hp,level)
        self.mana = mana
    @log_action
    def attack(self, target):
        if self.mana >=10:
            self.mana -=10
            target.take_damage(20)
        else:
            super().attack(target)
        
    def __str__(self):
        return f"{super().__str__()} MP {self.mana}"


class HealerMixin:
    @log_action
    def heal(self, target, amount):
        target.hp = min(target.max_hp, target.hp + amount)

class Priest(HealerMixin, Mage):
    pass

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, **item):
        self.items.append(item)

    def find(self, **filters):
        results = []
        for i in self.items:
            if all(i[k] == v for k, v in filters.items()):
                results.append(i)
        return results
                
    def __len__(self):
        return len(self.items)

tariel = Warrior("Tariel", hp=120, strength=15)
nestan = Mage("Nestan", hp=80, mana=50)

tariel.attack(nestan)

print(nestan)
print(nestan.is_alive)
print(Character.count)