class Character:
    count = 0

    def __init__ (self, name, hp=100, level=1):
        self.name = name
        self.hp = hp
        self.level = level
        Character.count +=1
    
    def __str__(self):
        return f"{self.name} (Lv { self.level}, HP {self.hp})"

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
    
    @property
    def is_alive(self):
        return self.hp > 0

a = Character("Tariel")
b = Character("Avtandil", hp=50)
b.take_damage(70)

print(a)
print(b)
print(b.is_alive)
print(Character.count)
