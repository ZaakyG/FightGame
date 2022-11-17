'''
By Isaac Gonzalez 11-16-2022
Player class.
Player will have several characters to play with, so the battles
are a player with 3 characters against a player with other 3 characters
or some kind of boss
'''
'''
TODOS write a class that inhabilitates dead chacters
'''

import character

class Player():
    '''
    '''
    def __init__(self,name,cname1,cname2,cname3,num1=1,num2=2,num3=3):
        self.name = name
        self.c1 = character.Character(cname1, num1)
        self.c2 = character.Character(cname2, num2)
        self.c3 = character.Character(cname3, num3)
        self.total_energy = self.c1.energy + self.c2.energy + self.c3.energy
        self.total_health = self.c1.health + self.c2.health + self.c3.health

    def consume_energy(self, points, skill, cha):
        if cha == 1:
            self.c1.consume_energy(points, skill)
        elif cha == 2:
            self.c2.consume_energy(points, skill)
        elif cha == 3:
            self.c3.consume_energy(points, skill)
        self.update_total_energy()

    def update_total_energy(self):
        self.total_energy = self.c1.energy + self.c2.energy + self.c3.energy
    
    def habilities_status(self):
        # print("-+----+------+-----+------+-----+------+----+")
        print("Your habilities have the following points: ")
        print("For {}: ".format(self.c1.name))
        print("Health: {}".format(self.c1.health))
        print("Strength: {}".format(self.c1.strength))
        print("Shield: {}".format(self.c1.shield))

        print("For {}: ".format(self.c2.name))
        print("Health: {}".format(self.c2.health))
        print("Strength: {}".format(self.c2.strength))
        print("Shield: {}".format(self.c2.shield))

        print("For {}: ".format(self.c3.name))
        print("Health: {}".format(self.c3.health))
        print("Strength: {}".format(self.c3.strength))
        print("Shield: {}".format(self.c3.shield))

    def select_attack(self, character):
        if character == 1:
            return self.c1.attack()
        elif character == 2:
            return self.c2.attack()
        elif character == 3:
            return self.c3.attack()

    def defend(self, character, points):
        if character == 1:
            self.update_total_health()
            return self.c1.defend(points)
        elif character == 2:
            self.update_total_health()
            return self.c2.defend(points)
        elif character == 3:
            self.update_total_health()
            return self.c3.defend(points)

    def update_total_health(self):
        self.total_health = self.c1.health + self.c2.health + self.c3.health

    def select_alive(self, character):
        if character == 1:
            return self.c1.character_dead()
        elif character == 2:
            return self.c2.character_dead()
        elif character == 3:
            return self.c3.character_dead()


'''
For console testing:
pl = player.Player()
'''