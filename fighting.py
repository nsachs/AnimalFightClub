import random

class Animal():
    def __init__(self):
        self.size = ''
        self.name = ''
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
        self.name = "bear"
        self.score = 0
        self.size = random.randrange(68, 78)
        self.speed = random.randrange(40, 50)
        self.health = 100
        self.strength = random.randrange(67, 72)
        self.weapon = random.randrange(67, 75)
        self.armor = random.randrange(61, 71)
        self.intelligence = random.randrange(31, 46)
        self.critical = 25


class Lion(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "lion"
        self.score = 0
        self.size = random.randrange(62, 72)
        self.speed = random.randrange(95, 100)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(80, 88)
        self.armor = random.randrange(40, 50)
        self.intelligence = random.randrange(43, 53)
        self.critical = 30


class Wolverine(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "wolverine"
        self.score = 0
        self.size = random.randrange(58,63)
        self.speed = random.randrange(40, 48)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(18, 25)
        self.armor = random.randrange(33, 43)
        self.intelligence = random.randrange(29, 39)
        self.critical = 17


class Alligator(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "alligator"
        self.score = 0
        self.size = random.randrange(50, 60)
        self.speed = random.randrange(18, 28)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(43, 51)
        self.armor = random.randrange(90, 100)
        self.intelligence = random.randrange(31, 39)
        self.critical = 25


class Black_cat(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "black_cat"
        self.score = 0
        self.size = random.randrange(40, 47)
        self.speed = random.randrange(40, 48)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(10, 16)
        self.armor = random.randrange(17, 27)
        self.intelligence = random.randrange(55, 61)
        self.critical = 5


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "dog"
        self.score = 0
        self.size = random.randrange(60, 65)
        self.speed = random.randrange(40, 65)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(18, 30)
        self.armor = random.randrange(25, 35)
        self.intelligence = random.randrange(38, 45)
        self.critical = 15


class Porcupine(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "porcupine"
        self.score = 0
        self.size = random.randrange(60, 65)
        self.speed = random.randrange(15, 25)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(25, 32)
        self.armor = random.randrange(60, 70)
        self.intelligence = random.randrange(28, 38)
        self.critical = 1


class Gorilla(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "gorilla"
        self.score = 0
        self.size = random.randrange(68, 78)
        self.speed = random.randrange(42, 49)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(28, 35)
        self.armor = random.randrange(62, 72)
        self.intelligence = random.randrange(82, 88)
        self.critical = 25

class Black_panther(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "black_panther"
        self.score = 0
        self.size = random.randrange(55, 65)
        self.speed = random.randrange(97,100)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(75, 85)
        self.armor = random.randrange(35, 45)
        self.intelligence = random.randrange(38, 45)
        self.critical = 30


class Elephant(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "elephant"
        self.score = 0
        self.size = random.randrange(84, 94)
        self.speed = random.randrange(50, 58)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(32, 47)
        self.armor = random.randrange(82, 92)
        self.intelligence = random.randrange(67, 73)
        self.critical = 28


class Giraffe(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "giraffe"
        self.score = 0
        self.size = random.randrange(55, 65)
        self.speed = random.randrange(35, 43)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(28, 35)
        self.armor = random.randrange(33, 43)
        self.intelligence = random.randrange(34, 43)
        self.critical = 23


class Rhino(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "rhino"
        self.score = 0
        self.size = random.randrange(75, 85)
        self.speed = random.randrange(39, 49)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(50, 60)
        self.armor = random.randrange(80, 90)
        self.intelligence = random.randrange(38, 45)
        self.critical = 30


class Bull(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "bull"
        self.score = 0
        self.size = random.randrange(80, 89)
        self.speed = random.randrange(80, 89)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(37, 43)
        self.armor = random.randrange(66, 76)
        self.intelligence = random.randrange(21, 31)
        self.critical = 30


class Human(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "human"
        self.score = 0
        self.size = random.randrange(35, 45)
        self.speed = random.randrange(35, 50)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(22, 28)
        self.armor = random.randrange(37, 47)
        self.intelligence = random.randrange(98, 100)
        self.critical = 20


class Cobra(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "cobra"
        self.score = 0
        self.size = random.randrange(60, 65)
        self.speed = random.randrange(25, 35)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(34, 40)
        self.armor = random.randrange(26, 36)
        self.intelligence = random.randrange(25, 35)
        self.critical = 80


class T_rex(Animal):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.name = "t-rex"
        self.score = 0
        self.size = random.randrange(90, 100)
        self.speed = random.randrange(65, 75)
        self.health = 100
        self.strength = random.randrange(80, 85)
        self.weapon = random.randrange(90, 95)
        self.armor = random.randrange(85, 95)
        self.intelligence = random.randrange(7, 13)
        self.critical = 20

bear = Bear()
lion = Lion()
wolverine = Wolverine()
alligator = Alligator()
black_cat = Black_cat()
cobra = Cobra()
dog = Dog()
porcupine = Porcupine()
gorilla = Gorilla()
black_panther = Black_panther()
elephant = Elephant()
giraffe = Giraffe()
rhino = Rhino()
bull = Bull()
human = Human()
t_rex = T_rex()

animal_list = [['bear', bear], ['lion',lion], ['wolverine', wolverine], ['alligator', alligator], ['black cat', black_cat], ['cobra', cobra], ['dog', dog], ['porcupine', porcupine], ['gorilla', gorilla], ["black panther", black_panther], ['elephant', elephant], ['giraffe', giraffe], ['rhino',rhino], ['bull',bull], ['human',human], ['T-rex',t_rex]]
animal = Animal()

lion = Lion()

bear = Bear()

turn = 100


def take_turn(animal1, animal2):
    winner = False
    while not winner:
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
if __name__ == '__main__':

    while not take_turn(lion, bear):
        print("Lion: " + str(lion.health), "Bear: " + str(bear.health))


        # if weapon - armor is negative just set it to 0
        # same with intelligece minus their intelligence
        # incorporate intelligence with critical and having the possibility for the damage to not hit
        # intelligence will increase with each win