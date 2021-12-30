#########################################################################################################
# This file contains ui screen of the game
#
#
#


import pygame
from variables import *
from fonts import *
from colors import * 
from animation import *  


class Ui:
        def __init__(self, window,age):
                self.window = window
                self.age = age
                
        def welcomeScreen(self):
                controls = textFont.render("press   ENTER   top  play   or  ESC  to quit", True, WHITE)
                controls2 = textFont.render("press  SHIFT   for    leaderboard", True, WHITE)
                controls2.set_alpha(blink())
                controls.set_alpha(blink())
                self.window.blit(controls, (WIDTH/4,HEIGHT*0.6))
                self.window.blit(controls2, (WIDTH/4,HEIGHT*0.68))
                # pygame.display.update()
                

        def gameTitle(self):
                W = titleFont.render("W",True, WHITE)
                ORD = titleFontOut.render("ORD",True, WHITE)
                G = titleFont.render("G",True, WHITE)
                UESSER = titleFontOut.render("UESSER",True, WHITE)
                self.window.blit(W,(WIDTH/3,HEIGHT/8))
                self.window.blit(G,(WIDTH/3+100,HEIGHT/3))
                self.window.blit(ORD, (WIDTH/3+100, HEIGHT/8))
                self.window.blit(UESSER, (WIDTH/3+180, HEIGHT/3))

        def gameDifficultyScreen(self):
                question = textFont.render("How   old   are   you?",True, WHITE)
                enter = textFont.render("Enter your age",True,WHITE)
                prompt = controlsFont.render("press  ENTER  to  select / BACKPACE to delete / ESC to go back to main screen",True,WHITE)

                self.window.blit(question,(WIDTH/3, HEIGHT*0.65))
                self.window.blit(enter,(WIDTH/3, HEIGHT*0.75))
                self.window.blit(prompt, (WIDTH/4, HEIGHT*0.9))
                self.age.drawWord()
                self.age.drawuserInput(textFont, HEIGHT*0.74 )