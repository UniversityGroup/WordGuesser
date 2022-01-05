###########################################By SyntaxError####################################################################################################
# Author: Ethan Ivey                                                                                                                                            #
#  This file contains different user interfaces for the game                                                                     #
#  functions:                                                                                                                                               #
#           welcomeScreen - gets a range of lines number of each difficulty level for example: easy difficulty words lies between line [2,97]           #
#           gameTitle           - pick a random number in a given range and pick a line.                                                                      #
#           gameDifficultyScreen                                                                                                                                                #
#           leaderboardScreen
#           gameplayScreen                                                                                                                                                #
#           gameOverScreen                                                                                                                                                #
#           warningScreen                                                                                                                                                       #
#           showResult                                                                                                                                                #
#############################################################################################################################################################


import pygame
from variables import *
from fonts import *
from colors import * 
from animation import *  
from input import Input

class Ui:
        def __init__(self, window):
                self.window = window
                #create cordinates for scores  
                self.cordinates = []
                
              
        def welcomeScreen(self):
                controls = textFont.render("press   ENTER   top  play   or  ESC  to quit", True, WHITE)
                controls2 = textFont.render("press  SHIFT   for    leaderboard", True, WHITE)
                controls2.set_alpha(blink())
                controls.set_alpha(blink())
                sound_control = textFont.render("left Ctrl toggle sound", True,WHITE)
                music_control = textFont.render("right Ctrl toggle music", True,WHITE)
                self.window.blit(controls, (WIDTH/4,HEIGHT*0.6))
                self.window.blit(controls2, (WIDTH/4,HEIGHT*0.68))
                self.window.blit(sound_control,(40 , HEIGHT*0.9))
                self.window.blit(music_control,(WIDTH*0.75 , HEIGHT*0.9))
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

                sound_control = textFont.render("left Ctrl toggle sound", True,WHITE)
                music_control = textFont.render("right Ctrl toggle music", True,WHITE)

                self.window.blit(question,(WIDTH/2.8, HEIGHT*0.15))
                
                self.window.blit(prompt, (WIDTH/4, HEIGHT*0.85))
                self.window.blit(easy, ((WIDTH/2.2, HEIGHT*0.35)))
                self.window.blit(medium, ((WIDTH/2.2, HEIGHT*0.45)))
                self.window.blit(hard, ((WIDTH/2.2, HEIGHT*0.55)))
                self.window.blit(sound_control,(40 , HEIGHT*0.9))
                self.window.blit(music_control,(WIDTH*0.75 , HEIGHT*0.9))


        def leaderboardScreen(self):
                if(len(self.cordinates) <= 0):
                        x = 1000
                        y = 400
                        y2 = 400
                        for i in range(10):
                                if(i < 5):
                                        self.cordinates.append([WIDTH-x,HEIGHT-y])
                                        y -= 75
                                        print(y)
                                else:
                                        x = 500
                                        self.cordinates.append([WIDTH-x,HEIGHT-y2])
                                        y2 -= 75

                        
                with open("scores.txt") as file:
                        lines = file.readlines()
                        if(len(lines) > 0):
                                for index,line in enumerate(lines):
                                        text = textFont.render(line,True,WHITE)
                                        self.window.blit(text,(self.cordinates[index][0]+40,self.cordinates[index][1]))
                                       
                                       
                highscores=titleFont.render("HighScores",True, WHITE)
                one=textFont.render("1.   ____________",True, WHITE)
                two=textFont.render("2.  ____________",True, WHITE)
                three=textFont.render("3.  ____________",True, WHITE)
                four=textFont.render("4.  ____________",True, WHITE)
                five=textFont.render("5.  ____________",True, WHITE)
                six=textFont.render("6.  ____________",True, WHITE)
                seven=textFont.render("7.   ____________",True, WHITE)
                eight=textFont.render("8.  ____________",True, WHITE)
                nine=textFont.render("9.  ____________",True, WHITE)
                ten=textFont.render("10.  ____________",True, WHITE)
                
                
                self.window.blit(highscores,(WIDTH-900, HEIGHT- 600))
                self.window.blit(one,(self.cordinates[0]))
                self.window.blit(two,(self.cordinates[1]))
                self.window.blit(three,(self.cordinates[2]))
                self.window.blit(four,(self.cordinates[3]))
                self.window.blit(five,(self.cordinates[4]))
                self.window.blit(six,(self.cordinates[5]))
                self.window.blit(seven,(self.cordinates[6]))
                self.window.blit(eight,(self.cordinates[7]))
                self.window.blit(nine,(self.cordinates[8]))
                self.window.blit(ten,(self.cordinates[9]))

        def gameplayScreen(self,level,lives,score,skips,availableHints,streak):
                difficulty=textFont.render("Difficulty : "+str(level),True, WHITE)
                score=textFont.render("Score : "+str(score),True, WHITE)
                streak=textFont.render("Streak : "+str(streak)[:3],True, WHITE)
                skip=textFont.render("Press \ to skip (skips available "+str(skips)+")",True, WHITE)
                chances=textFont.render("   chances remain: "+str(lives),True, WHITE)
                missing_line=textFont.render("enter the missing letter ",True, WHITE)
                sound_control = textFont.render("left Ctrl toggle sound", True,WHITE)
                music_control = textFont.render("right Ctrl toggle music", True,WHITE)
                hint_available = textFont.render("Press TAB to show hints",True,WHITE)
                hints = textFont.render("Hints available: "+str(availableHints),True,WHITE)
                
                
                self.window.blit(difficulty,(WIDTH*0.05 , HEIGHT*0.05))
                self.window.blit(score,(WIDTH*0.75 , HEIGHT*0.05))
                self.window.blit(streak,(WIDTH*0.75, HEIGHT*0.15))
                self.window.blit(skip,(WIDTH*0.3 , HEIGHT*0.9))
                self.window.blit(chances,(WIDTH*0.4, HEIGHT*0.05))
                self.window.blit(missing_line,(WIDTH*0.35 , HEIGHT*0.8))
                self.window.blit(sound_control,(40 , HEIGHT*0.9))
                self.window.blit(music_control,(WIDTH*0.75 , HEIGHT*0.9))
                self.window.blit(hint_available,(WIDTH*0.35 , HEIGHT*0.7))
                self.window.blit(hints,(WIDTH*0.05 , HEIGHT*0.15))
        


        def gameOverScreen(self,score):
                message = textFont.render("Your score: "+str(score),True,WHITE)
                message2 = textFont.render("To save your score enter your name",True,WHITE)
                self.window.blit(message,(WIDTH/2.5,HEIGHT*0.2))
                self.window.blit(message2,(WIDTH/3,HEIGHT*0.3))

        def warningScreen(self, highlight):
                message = textFont.render("Are you sure you want to quit? this will reset your progress", True, RED)
                if(highlight == 0):
                        cancel = textFont.render("Cancel",True, RED)
                else:
                        cancel = textFont.render("Cancel",True, WHITE)
                if(highlight == 1):
                        quit = textFont.render("Quit",True, RED)
                else:
                        quit = textFont.render("Quit",True, WHITE)

                self.window.blit(message, (WIDTH*0.15,HEIGHT*0.20))
                self.window.blit(cancel, (WIDTH*0.35,HEIGHT*0.45))
                self.window.blit(quit, (WIDTH*0.6,HEIGHT*0.45))

        def showResult(self, answer, word,level,lives,score,streak):
                answer_string = ""
                word_string = ""
                for x in answer:
                        answer_string += x
                for x in word:
                        word_string += x

                #if guessed correct say its correct answer
                if(answer_string.lower() == word_string.lower()):
                        correct = textFont.render("Correct!",True, LIGHT_GREEN)
                        self.window.blit(correct, (WIDTH*0.45,HEIGHT*0.3))
                else:
                        wrong = textFont.render("Wrong!",True, RED)
                        self.window.blit(wrong, (WIDTH*0.45,HEIGHT*0.3))

                text = textFont.render("Actual answer: "+answer_string,True, WHITE)
                text2 = textFont.render("Your answer: "+word_string,True, WHITE)
                difficulty=textFont.render("Difficulty : "+str(level),True, WHITE)
                score=textFont.render("Score : "+str(score),True, WHITE)
                streak=textFont.render("Streak : " +str(streak)[:3],True, WHITE)
                skip=textFont.render("Press Enter to continue ",True, WHITE)
                chances=textFont.render("   chances remain: "+str(lives),True, WHITE)
                self.window.blit(difficulty,(WIDTH*0.05 , HEIGHT*0.05))
                self.window.blit(score,(WIDTH*0.75 , HEIGHT*0.05))
                self.window.blit(streak,(WIDTH*0.75, HEIGHT*0.15))
                self.window.blit(skip,(WIDTH*0.4 , HEIGHT*0.9))
                self.window.blit(chances,(WIDTH*0.3, HEIGHT*0.05))
                self.window.blit(text,(WIDTH*0.4,HEIGHT*0.45))
                self.window.blit(text2, (WIDTH*0.4, HEIGHT*0.55))                
                


                
                