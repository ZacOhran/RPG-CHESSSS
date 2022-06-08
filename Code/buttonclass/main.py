import pygame







pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
running = True
BLACK = (0, 0, 0)
FPS = 60


battlescreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


class Background:

    BACKGROUND = pygame.image.load('bbg.png')

    def __init__(self):
        self.clock = pygame.time.Clock()

    def battleupdate(self):
        battlescreen.fill(BLACK)
        battlescreen.blit(self.BACKGROUND, (0, 0))
        # battle.drawing()
        pygame.display.update()
        self.clock.tick(FPS)


"""class ButtonController:
    def __init__(self):
        #Create ATK buttons
        self.atk_button = Button(battlescreen,height = 20, width = 40, command=self.ATK_func)
        self.target1_button = Button(battlescreen, height = 20, width = 40, command=self.ATK_T1_func())
        self.target2_button = Button(battlescreen, height = 20, width = 40, command=self.ATK_T2_func())
        self.target3_button = Button(battlescreen, height = 20, width = 40, command=self.ATK_T3_func())
        #Create abilty buttons
        self.ability_button = Button(battlescreen, height = 20, width = 40, command=self.ability_func())
        self.target1_button = Button(battlescreen, height = 20, width = 40, command=self.ability_T1_func())
        self.target2_button = Button(battlescreen, height = 20, width = 40, command=self.ability_T2_func())
        self.target3_button = Button(battlescreen, height = 20, width = 40, command=self.ability_T3_func())

    def draw_buttons(self):
        #draw all buttons with if statements?
        self.atk_button.place(battlescreen, x=100, y=100)
        self.target1_button.place(battlescreen, x=140, y=180)
        self.target2_button.place(battlescreen, x=180, y=260)
        self.target3_button.place(battlescreen, x=220, y=340)

        self.ability_button.place(battlescreen, x=260, y=380)
        self.target1_button.place(battlescreen, x=300, y=460)
        self.target2_button.place(battlescreen, x=3400, y=540)
        self.target3_button.place(battlescreen, x=380, y=620)"""


# ATK control

def ATK_func():
    active_atk_button = True
    while active_atk_button:
        #draw target buttons
        pass

def ATK_T1_func():
    # call attacker's attack function on target1
    pass

def ATK_T2_func():
    # call attacker's attack function on target1
    pass

def ATK_T3_func():
    # call attacker's attack function on target1
    pass


#Ability control

def ability_func():
    active_ability_button = True
    while active_ability_button:
        #draw target buttons
        pass

def ability_T1_func():
    # call attacker's attack function on target1
    pass

def ability_T2_func():
    # call attacker's attack function on target1
    pass

def ability_T3_func():
    # call attacker's attack function on target1
    pass








if __name__ == '__main__':
    bg = Background()
    buttonControl = ButtonController()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg.battleupdate()
        buttonControl.draw_buttons()
        pygame.display.update()
        clock.tick(FPS)