from player import *
import random
from stats import *

#ignore this file for now not complete




class Troops:

    def __init__(self, character_name):
        #target type?
        #graphics setup - drawing the dudes on chess board if u want
        self.character = character_name
        troop_stat = TROOP_STATS[self.character]
        self.HP = troop_stat['HP']
        self.ATK = troop_stat['ATK']
        self.DEF = troop_stat['DEF']
        self.MGA = troop_stat['MGA']
        self.MGD = troop_stat['MGD']
        self.CRIT = troop_stat['CRIT']
        self.MGP = troop_stat['MGP']
        self.SPD = troop_stat['SPD']



    def attack(self, target):
        # Will check target DEF and run through DMG formula to get resulting damage value. Will then reduce Target HP by results. 
        r = random.randint(0, 100)
        print(r)
        if r <= self.CRIT:
            # no crit
            damage = (int(self.ATK/target.DEF)^2 * 50)
            damage = (damage)
            target.HP_reduction(damage)
            print(f"Targets HP is reduced by {damage}")
        else:
            # yes crit
            damage = (int(self.ATK/target.DEF)^2 * 75)
            damage = (damage)
            target.HP_reduction(damage)
            print(f"Critical Strike! Targets HP is reduced by {damage}")

    def HP_reduction(self, damage):
        self.HP -= damage
        print(self.HP)
        return self.HP

class Knight(Troops):
    # add abilities here
    def SuperATK(self, target):
        r1 = random.randint(0, 100)
        print(r1)
        if r1 >= self.CRIT:
            # no crit
            damage = (int(self.ATK/target.DEF)^2 * 100)
            damage = (damage)
            target.HP_reduction(damage)
            print(f"Targets HP is reduced by {damage}")
        else:
            # yes crit
            damage = (int(self.ATK/target.DEF)^2 * 150)
            damage = (damage)
            target.HP_reduction(damage)
            print(f"Critical Strike! Targets HP is reduced by {damage}")


    def DefenceUp(self):
        # find way to increase DEF for 3 turns? maybe figure out that timing first.
        pass

class Monster1(Troops):
    # add abilities here
    pass



zac = Knight('Knight')
connor = Knight('Knight')

zac.SuperATK(connor)
print(f"CONNORS HP IS {connor.HP}")
