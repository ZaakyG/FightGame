'''
This is the character class for the video game
Here, things such as player definition, hp, shield... and so on
are defined so that a player may have the desired characteristics he wants
as well as a worthy opponent.
'''

class Character():
    '''
    Character class where properties such as
    health points, strength, shield, and energy.
    Also, methods to attack, decrease health when 
    attacked, and also gain energy
    '''
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.health = 200
        self.strength = 25     
        self.shield = 10 
        self.energy = 50       
        
        
    def attack(self):
        self.earn_energy(1)
        return self.strength
    
    def defend(self, attack_in):
        self.earn_energy(2)
        total_attack = self.shield - attack_in
        self.health += total_attack
    
    def consume_energy(self, points, skill):
        if skill == 1:
            self.health += points * 1.5
            self.energy += (-points)
            return self.health
        elif skill == 2:
            self.strength += points
            self.energy += (-points)
            return self.strength
        elif skill == 3:
            self.shield += points
            self.energy += (-points)
            return self.shield
        else:
            print("Not a valid optison.")
            return 0

    def earn_energy(self, action):
        if action == 1: # means attack
            self.energy += 5
        elif action == 2: # means defend
            self.energy += 10

    def character_dead(self):
        '''
        A character method that makes the character dead
        that should mean that the character is not 
        able to interact anymore
        '''
        if self.health <= 0:
            return True
        else:
            return False
