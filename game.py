'''
By Isaac Gonzalez 11-16-2022
'''

import player
import character
import random

'''
TODO
Fix bugs like:
- DONE: When a character is dead it should not be able to interact anymore 
- DONE: Every 3 turns the player can decide how to spend character energy
- A play again button must be implemented
'''

class Game():
    '''
    Actual game class
    '''
    def __init__(self, player_name, cname1, cname2, cname3):
        # self.character = character.Character(player_name)
        # self.name = player_name
        self.player1 = player.Player(player_name, cname1, cname2, cname3)
        self.Boss = character.Character("The Beast", 1)

        # Set up Boss 
        self.Boss.health = 500
        self.Boss.strength = 50
        self.Boss.shield = 15

    # Consider deleting main_game method
    def main_game(self):
        pass

    def pre_battle(self):
        """
        Pre battle stage where energy points are used before game starts
        """
        while self.player1.total_energy > 0:
            self.energy_usage(0)
        self.player1.habilities_status() 

    def battle(self):
        turn = 0
        print("--------------- Battle begins ------------")
        while self.player1.total_health > 0 and self.Boss.health > 0:

            num = input("Enter the character you want to use: ")
            while self.player1.select_alive(int(num)) == True:
                print("The charachter you selected is dead, choose another one:")
                num = input("Enter the character you want to use: ")
            att = self.player1.select_attack(int(num))
            self.Boss.defend(att)
            print("You make an attack with {} points".format(att)) 
            print(self.Boss.health,"points remaining in boss.") 
            # print(self.player1.select_attack(int(num)))

            # Boss fights back
            print("-=-=-= Boss fights back -=-=-=")
            boss_attc = self.Boss.attack()
            boss_select_character = random.randint(1,3)
            self.player1.defend(boss_select_character, boss_attc)

            # To test, delete afterwards:
            # self.player1.defend(1, boss_attc)
            # self.player1.habilities_status()
            turn += 1
            self.energy_usage(turn)

        if self.player1.total_energy > 0:
            print(self.player1.name, "wins!!")
        else:
            print("Boss wins")

    def energy_usage(self, turn):
        if turn % 3 == 0:
            print("-----------------------------------------------")
            print("1) You have",self.player1.c1.energy,"points for",self.player1.c1.name)
            print("2) You have",self.player1.c2.energy,"points for",self.player1.c2.name)
            print("3) You have",self.player1.c3.energy,"points for",self.player1.c3.name)
            print("Choose how to spend your energy points")
            print("Health points are increased 1x1.5 energy points")
            print("Strenght and shield points are exchanged 1x1")
            num = input("Enter the your character number: " )
            points = input("Enter how many points: ")
            skill = input("Enter skill number: ")
            new_points = self.player1.consume_energy(float(points), int(skill), int(num))
            print("Remaining hability points for character {} : {}".format(num, new_points))
        else:
            pass

        

gam = Game("Isaac", "Sword", "Archer", "Horse")
gam.pre_battle()
gam.battle()
