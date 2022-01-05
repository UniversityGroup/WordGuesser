######################################by SyntaxError#########################################################################################
#  Author: Sandip Pradhan (24899810)
#  Input sytem - recoreds user inputs, draws cursor at screen, draw text into screen, compares the result and answer                        #
#  Functions:                                                                                                                               #
#               missingLetterCount - calculates number of letter missing from puzzle,                                                       #
#               letterCordinates   - calculate x cordinate of each letter, draw a cursor at focused area                                    #
#               firstCursor        - calculate where the first cursor should be                                                             #
#               drawCursor         - calculate and draw where the cursor should be                                                          #
#               drawWord           - draws the puzzule into the screen                                                                      #
#               nextPosition       - update position of cursor when key is pressed                                                          #
#               deleteLetter       - delete letter from puzzle when backspace is pressed                                                    #
#               userInput          - record user input and save it                                                                          #
#               drawuserInput      - draw the key user pressed                                                                              #
#               nextWord           - choose the next puzzle                                                                                 #
#               constructWord      - adds the user inputed key with missing letter array to form a word array                               #
#                                                                                                                                           #
#############################################################################################################################################


from typing import Counter
import pygame
from animation import blink
from variables import *
from fonts import *
from colors import *
class Input:
    def __init__(self, stringArray, window, startX, startY):
        pygame.init()
        self.string = stringArray
        self.window = window
        self.length = len(stringArray)
        self.startX = startX
        self.startY = startY
        #list of xPos of each letter eg [400,450,500]
        self.cordinates = []
        #index of missing letters for exmaple "t _ _ t" = [1,2]
        self.missingPosition = []
        self.index = 0
        self.cursorPos = self.index
        self.keys = {}
        self.counter = 0
        self.letterCordinates()
        self.firstCursor()
        self.missingLetterNumber = self.missingLetterCount()
        
        
        

    #count missing letters
    def missingLetterCount(self):
        count = 0
        for index, letter in enumerate(self.string):
            if(letter == "_"):
                count += 1
                self.missingPosition.append(index)
        return count

    #calculate letter cordinates
    def letterCordinates(self):
        xPos = self.center()
        spacing = 25
        for letter in self.string:
            xPos += gameplayFont.size(letter)[0]+spacing
            self.cordinates.append(xPos)
        
    #calculate where the first cursor should be
    def firstCursor(self):
        for index,letter in enumerate(self.string):
            if(letter == "_"):
                self.index = index
                
                return

    #draw cursor at focused area
    def drawCursor(self):
        cursor = gameplayFont.render("|", True, WHITE)
        cursor.set_alpha(blink())
        #draw cursor at end of character if there is a letter in current position
        if(self.missingPosition[self.cursorPos] in self.keys):
            self.window.blit(cursor, (self.cordinates[self.missingPosition[self.cursorPos]]+ gameplayFont.size(self.keys[self.missingPosition[self.cursorPos]])[0], self.startY))
        else:
            self.window.blit(cursor, (self.cordinates[self.missingPosition[self.cursorPos]], self.startY))

    #draw the word
    def drawWord(self):
        for index,letter in enumerate(self.string):
            font = gameplayFont.render(letter, True, WHITE)
            self.window.blit(font, (self.cordinates[index], self.startY))
        self.drawCursor()


    #move cursor when key is pressed 
    def nextPosition(self):
        if(self.index < self.length - 1):
            self.index += 1

            

    #delete words when backspace is pressed
    def deleteLetter(self):
        if(self.index > 0):
            self.index -= 1
        if(self.counter > 0):
            self.counter -= 1
            self.keys.pop(self.missingPosition[self.counter])
            
        
        
        
        

    #get and save user input
    def userInput(self, key):
        if(self.string[self.missingPosition[self. counter]] == "_"):
            self.keys[self.missingPosition[self.counter]] = key
        
       

    #draw user input
    def drawuserInput(self,font, y):
        if(len(self.keys) > 0):
            for key, value in self.keys.items():
                text = font.render(value, True, WHITE)
                self.window.blit(text, (self.cordinates[key], y))

    def nextWord(self, stringArray):
        self.string = stringArray
        self.length = len(stringArray)
        #list of xPos of each letter eg [400,450,500]
        self.cordinates = []
        #index of missing letters for exmaple "t _ _ t" = [1,2]
        self.missingPosition = []
        self.index = 0
        self.counter = 0
        self.keys = {}
        self.cursorPos = self.index
        self.letterCordinates()
        self.firstCursor()
        self.missingLetterNumber = self.missingLetterCount()

    #add the user input with self.string to create a result array   
    def constructWord(self):
        for key, value in self.keys.items():
            self.string[key] = value
        return self.string

    #create a user input string
    def constructString(self):
        self.constructWord()
        result = ""
        for x in self.string:
            if(x != "_"):
                result += x
        return result

    #render hint
    def renderHint(self, hint):
        hintText = textFont.render("Hint: "+hint, True, WHITE)
        wordLength = 0
        for x in hint:
            wordLength += textFont.size(x)[0]
        

        self.window.blit(hintText,((WIDTH-wordLength)/2,HEIGHT/1.8))

    #calculate where the text gonna be in center
    def center(self):
        x = 0
        for letter in self.string:
            x += gameplayFont.size(letter)[0] 
        return (WIDTH - x)/2.5
        




