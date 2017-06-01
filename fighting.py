animal_list = ['bear', 'lion', 'wolverine', 'alligator', 'black cat', 'cobra', 'dog', 'porcupine', 'gorilla', 'lion',
               'black panther', 'elephant', 'giraffe', 'rhino', 'bull', 'human', 'T-rex']


class Animal():
    def __init__(self):
        self.size = ''
        self.speed = ''
        self.health = ''
        self.strength = ''
        self.weapon = ''
        self.armor = ''
        self.intelligence = ''
        self.critical = ' '


class Bear(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(68, 78)
        self.speed = random.randrange(55, 60)
        self.health = 100
        self.strength = random.randrange(67, 72)
        self.weapon = random.randrange(84, 89)
        self.armor = random.randrange(58, 63)
        self.intelligence = random.randrange(75, 80)
        self.critical = random.randrange(60, 65)


class Lion(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(62, 72)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Wolverine(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(20, 35)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Alligator(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(50, 60)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Black_cat(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(60, 65)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(60, 65)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Porcupine(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(60, 65)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Gorilla(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(68, 78)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Black_panther(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(55, 65)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Elephant(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(84, 94)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Giraffe(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(55, 65)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Rhino(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(75, 85)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Bull(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(64, 74)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Human(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(35, 45)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class Cobra(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(60, 65)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


class T_rex(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score = 0
        self.size = random.randrange(90, 100)
        self.speed = random.randrange(50, 55)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(65, 70)
        self.armor = random.randrange(40, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = random.randrange(80, 85)


animal = Animal()

import random

lion = Lion()

bear = Bear()

turn = 100


def take_turn(animal1, animal2):
    winner = False
    animal2.turn += animal2.speed
    animal1.turn += animal1.speed
    if animal1.turn >= 100:
        number = random.randrange(100 - animal1.critical)
        winner = fight(animal1, animal2, number)
        animal1.turn -= 100
    if animal2.turn >= 100:
        number = random.randrange(100 - animal2.critical)
        winner = fight(animal2, animal1, number)
        animal2.turn -= 100
    print(winner)
    print(animal1.health)
    print(animal2.health)
    return winner


def fight(attack, defense, number):
    if attack.health > 0 and defense.health > 0:
        critical = 1
        if number == 5:
            critical = 2
        weapon_defense = attack.weapon - defense.armor
        if weapon_defense < 0:
            weapon_defense = 0
        intelligence_comparison = attack.intelligence - defense.intelligence
        if intelligence_comparison < 0:
            intelligence_comparison = 0
        damage = round(((attack.strength + weapon_defense + intelligence_comparison)) / 5 * critical)
        defense.health -= damage

    if defense.health <= 0:
        return attack
    else:
        return False


'''
STUFF FOR LATER
if attack.health > 0:
    #attack.intelligence += 5
    winner = attack
else:
    defense.intelligence += 5
    winner = defense
'''

while not take_turn(lion, bear):
    print("Lion: " + str(lion.health), "Bear: " + str(bear.health))


    # if weapon - armor is negative just set it to 0
    # same with intelligece minus their intelligence
    # incorporate intelligence with critical and having the possibility for the damage to not hit
    # intelligence will increase with each win