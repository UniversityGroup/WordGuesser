########################################################
#  class to accept and render user input

import pygame
from fonts import *
from colors import WHITE
from variables import *
from animation import *

class InputSystem:

    def __init__(self, string,missingLetters,window):
        pygame.init()
        #guessing word
        self.string = string
        #main graphics window
        self.window = window
        #length of the guessing word
        self.length = len(string)
        #missing letter from guess word
        self.missingLetters = missingLetters
        #position where the letters missing from word
        self.missingPosition = None
        #starting x position of the word 
        self.startX = WIDTH/3
        #starting y position of the word
        self.startY = HEIGHT/3
        #spacing between each letter
        self.letterSpacing = 0
        #spacing between the cursior
        self.xSpacing = 0
        #array of positions of missing letters
        self.focusArray = []
        self.i  = -1
        #user input
        self.keys = {}
        #starting index
        self.index = 0
        #number of missing letters
        self.count = 0
        #current letter
        self.letter = None
        #return missng letters count
        self.missingLetterCount()
        #is first focusPoisition calculate
        self.initial = False
        #x position of missing letter
        self.xPos = []

    #draw blinking cursor at focused area
    def drawCursor(self, pos):
        line = gameplayFont.render("|",True,WHITE)
        line.set_alpha(blink())
        self.window.blit(line,pos)

    #return missng letters count
    def missingLetterCount(self):
        for letter in self.string:
            if(letter == "_"):
                self.count += 1

    #calculate which letter to focus on
    def getFocusPosition(self):
        for index, letter in enumerate(self.string):
            # if(self.focusPosition < index and letter == "_"):
            #     print("focusp before "+str(self.focusPosition))
            #     self.focusPosition = index
            #     print("focusp after "+str(self.focusPosition))
            #     self.focusArray.append(index)
                
            #     self.letter = "_"
            #     self.xPos.append(self.calculateXPos(self.focusPosition))
            #     return
            if(self.index < index and letter == "_"):
                self.focusArray.append(index)
                self.xPos.append(self.calculateXPos(index))
                
                



    def deleteCharacter(self):
        if(len(self.keys) > 0):
            self.keys.pop(self.focusArray[self.i])
            self.focusArray.remove(self.focusArray[self.i])
    
            
        
        
    
    #insert letter to focused area
    def insertLetter(self):
        i = 0
        for key, value in self.keys.items():
            font = gameplayFont.render(value, True, WHITE)
            self.window.blit(font,(self.startX + self.xPos[i], self.startY))
            i += 1
            
            
    #calculate x position of a letter
    def calculateXPos(self, position):
        result = 0
        for x in range(position):
            result += gameplayFont.size(self.string[x])[0]+20

        return result

    #draw the user input at correct position
    def drawInput(self):
        self.letterSpacing = 0
        for index, letter in enumerate(self.string):
            font = gameplayFont.render(letter,True,WHITE)
            self.window.blit(font, (self.startX+self.letterSpacing,self.startY))
            self.letterSpacing += gameplayFont.size(letter)[0]+20
            if(not self.initial):
                self.getFocusPosition()
                self.initial = True
            # print(self.index, self.focusArray)
            if(letter == "_" and index == self.focusArray[self.index]):
                self.xSpacing = 0
               
                for x in self.string[0:self.focusArray[self.index]]:

                    self.xSpacing += gameplayFont.size(x)[0]+20
                 
                        
                     
                 
                
                self.drawCursor((self.startX+self.xSpacing,self.startY))
                    


    def next(self, string, missingLetters):
        #guessing word
        self.string = string
        #length of the guessing word
        self.length = len(string)
        #missing letter from guess word
        self.missingLetters = missingLetters
        #position where the letters missing from word
        self.missingPosition = None
        #user input
        self.keys = {}
        #starting index
        self.index = 0
        #number of missing letters
        self.count = 0
        #current letter
        self.letter = None
        #return missng letters count
        self.missingLetterCount()
        #is first focusPoisition calculate
        self.initial = False
        #x position of missing letter
        self.xPos = []


        pygame.display.update()
    
