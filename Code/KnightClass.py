from player import *
import random







class Knight:


    def __init__(self, HP, ATK, DEF, MGA, MGD, MGP, SPD, CR):
        # super().__init__()
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.MGA = MGA
        self.MGD = MGD
        self.MGP = MGP
        self.SPD = SPD
        self.CRIT = CR


    """
    @proPerty
    def ATK(self):
        ATK = self.ATK
        return ATK

    @property
    def DEF(self):
        DEF = self.DEF
        return DEF

    @property
    def HP(self):
        HP = self.HP
        return HP

    @property
    def MGA(self):
        MGA = self.MGA
        return MGA

    @property
    def MGD(self):
        MGD = self.MGD
        return MGD

    @property
    def MGP(self):
        MGP = self.MGP
        return MGP

    @property
    def SPD(self):
        return self.SPD
        """



    def attack(self, target):
        # Will check target DEF and run through DMG formula to get resulting damage value. Will then reduce Target HP by results. 
        r = random.randint(0, 100)
        print(r)
        if r <= self.CRIT:
            # no crit
            damage = int(int(self.ATK/target.DEF)^2 * 50)
            damage = int(damage)
            target.HP_reduction(damage)
            print(f"Targets HP is reduced by {damage}")
        else:
            # yes crit
            damage = int(int(self.ATK/target.DEF)^2 * 75)
            damage = int(damage)
            target.HP_reduction(damage)
            print(f"Targets HP is reduced by {damage}")
        pass

    def HP_reduction(self, damage):
        self.HP -= damage
        print(self.HP)



HP = 10000
ATK = 10
DEF = 10
MGA = 0
MGD = 10
MGP = 0
SPD = 5
CR = 20
zac = Knight(HP, ATK, DEF, MGA, MGD, MGP, SPD, CR)
connor = Knight(HP, ATK, DEF, MGA, MGD, MGP, SPD, CR)

zac.attack(connor)
print(f"CONNORS HP IS {connor.HP}")
