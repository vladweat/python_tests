from random import random, randint

class Warrior:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def setDamage(self, damage):
        self.health -= damage

    def checkHealth(self):
        if self.health > 0:
            return "'s health is {}".format(self.health)
        else:
            return " is dead"

warrior1 = Warrior("War1", 100)
warrior2 = Warrior("War2", 100)

while warrior1.health > 0 and warrior2.health > 0:

    print("\nNext round\n")

    if random() < 0.5:
        damage = randint(1, 20)
        warrior1.setDamage(damage)
        print("Warrior2 deal {} damage to Warrior1. Warrior1 has {} hp!".format(damage, warrior1.health))
    else:
        damage = randint(1, 20)
        warrior2.setDamage(damage)
        print("Warrior1 deal {} damage to Warrior2. Warrior2 has {} hp!".format(damage, warrior2.health))

    print("Warrior1", warrior1.checkHealth(), ", Warrior2", warrior2.checkHealth())

if warrior1.health > 0:
    print("Warrior1 wins!")
elif warrior2.health > 0:
    print("Warrior2 wins!")
else:
    print("Draw!")