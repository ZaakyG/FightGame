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
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.strength = 25     
        self.shield = 10 
        self.energy = 0       
        
    def attack(self):
        self.earn_energy(1)
        return self.strength
    
    def defend(self, attack):
        self.earn_energy(2)
        total_attack = self.shield - attack
        self.health += total_attack
    
    def consume_energy(self, points, skill):
        if skill == "health":
            self.health += points * 1.5
        elif skill == "strength":
            self.strength += points
        elif skill == "shield":
            self.shield += points

    def earn_energy(self, action):
        if action == 1: # means attack
            self.energy += 5
        elif action == 2: # means defend
            self.energy += 10

