'''
This is the character class for the video game
Here, things such as player definition, hp, shield... and so on
are defined so that a player may have the desired characteristics he wants
as well as a worthy opponent.
'''
class Character():
    def __init__(self):
        self.health = 200
        self.strength = 25     
        self.shield = 10 
        self.energy = 0       
        
    def attack(self):
        return self.strength
    
    def defend(self, attack):
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
