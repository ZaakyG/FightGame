'''
Player class.
Player will have several characters to play with, so the battles
are a player with 3 characters against a player with other 3 characters
or some kind of boss
'''
import character

class Player():
    '''
    '''
    def __init__(self, name, cname1, cname2, cname3):
        self.name = name
        self.c1 = character.Character(cname1)
        self.c2 = character.Character(cname2)
        self.c3 = character.Character(cname3)
