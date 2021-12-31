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
        def __init__(self, window):
                self.window = window
              
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

        def gameDifficultyScreen(self,highlight):
                question = textFont.render("Choose game difficulty",True, WHITE)
                prompt = controlsFont.render("press  ENTER  to  select / Arrows to scroll / ESC to go back to main screen",True,WHITE)
                #highlight easy if 0
                if(highlight == 0):
                        easy = textFont.render("Easy",True, LIGHT_GREEN)
                else:
                        easy = textFont.render("Easy",True, WHITE)
                #highlight medium if 1
                if(highlight == 1):
                          medium = textFont.render("Medium",True, LIGHT_GREEN)
                else:        
                        medium = textFont.render("Medium",True, WHITE)
                #highlight hard if 2
                if(highlight == 2):
                         hard = textFont.render("Hard",True, LIGHT_GREEN)
                else:
                        hard = textFont.render("Hard",True, WHITE)
                self.window.blit(question,(WIDTH/2.8, HEIGHT*0.15))
                
                self.window.blit(prompt, (WIDTH/4, HEIGHT*0.9))
                self.window.blit(easy, ((WIDTH/2.2, HEIGHT*0.35)))
                self.window.blit(medium, ((WIDTH/2.2, HEIGHT*0.45)))
                self.window.blit(hard, ((WIDTH/2.2, HEIGHT*0.55)))


        def leaderboardScreen(self):
                
                highscores=titleFont.render("HighScores",True, WHITE)
                one=textFont.render("1.   ____________",True, WHITE)
                two=textFont.render("2.   ____________",True, WHITE)
                three=textFont.render("3.   ____________",True, WHITE)
                four=textFont.render("4.   ____________",True, WHITE)
                five=textFont.render("5.   ____________",True, WHITE)
                six=textFont.render("6.   ____________",True, WHITE)
                seven=textFont.render("7.   ____________",True, WHITE)
                eight=textFont.render("8.   ____________",True, WHITE)
                nine=textFont.render("9.   ____________",True, WHITE)
                ten=textFont.render("10.   ____________",True, WHITE)
                
                
                self.window.blit(highscores,(WIDTH-900, HEIGHT- 600))
                self.window.blit(one,(WIDTH-1000, HEIGHT- 400))
                self.window.blit(two,(WIDTH-1000, HEIGHT- 325))
                self.window.blit(three,(WIDTH-1000, HEIGHT- 250))
                self.window.blit(four,(WIDTH-1000, HEIGHT- 175))
                self.window.blit(five,(WIDTH-1000, HEIGHT- 100))
                self.window.blit(six,(WIDTH-500, HEIGHT- 400))
                self.window.blit(seven,(WIDTH-500, HEIGHT- 325))
                self.window.blit(eight,(WIDTH-500, HEIGHT- 250))
                self.window.blit(nine,(WIDTH-500, HEIGHT- 175))
                self.window.blit(ten,(WIDTH-500, HEIGHT- 100))

        def gameplayScreen(self):
                time=textFont.render("Time :",True, WHITE)
                self.window.blit(time,(WIDTH*0.5 , HEIGHT- 400))
                
                