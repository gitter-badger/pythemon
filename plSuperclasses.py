"""Player Superclass"""

class Character(object):
    """Primary class for all character subclasses"""
    def __init__(self, name):
        self.name = name

class NPC(Character):
    """NPC superclass"""
    def __init__(self):
        super(NPC, self).__init__()
        #todo

class Player(object):
    """The Player (AKA "Player 1", "Main Character", "The One that Always Wins")"""
    def __init__(self):
        super(Player, self).__init__()
        #todo
        