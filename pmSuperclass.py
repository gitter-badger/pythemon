"""Contains the superclasses for all Pokemon/NPC/Player subclasses"""

class Pokemon(object):
    """docstring for Pokemon"""
    def __init__(self, name, health, attack, defense, spAttack, spDefense, speed, evoNum, num):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.spAttack = spAttack
        self.spDefense = spDefense
        self.speed = speed
        self.evoNum = evoNum
        self.num = num
    def use(self, attack):
        #todo
        print 'yey'
