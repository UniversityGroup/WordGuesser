######################################by SyntaxError#########################################################################################
#  Main file - program starting                                                                                                             #
#  Functions: Creates a window to display, install pygame if not present, Drawing into the display                                          #
#                                                                                                                                           #
#                                                                                                                                           #
#                                                                                                                                           #
#                                                                                                                                           #
#                                                                                                                                           #
#############################################################################################################################################

import os
import sys
try:
    import pygame
    import pygame.time
except:
    print("Pygame not installed Trying to install pygame.....")
    if(sys.platform == "linux" or sys.platform == "darwin"):
        os.system("python3 -m pip install pygame")
        
    else:
        os.system("python -m pip install pygame")
        
import pygame
import pygame.time
from colors import *
from variables import *
from fonts import *
from animation import *
from input import Input
from wordSplitter import wordSplitter
from score import Score
from ui import Ui



#Game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Game window title
pygame.display.set_caption("Render")
word = None
input = None

gameUi = Ui(WIN)
#highlight for level selection 
highlight = 0

def updateScreen():
    pygame.display.update()

def draw():
    WIN.fill(BACKGROUND_COLOR)
    x = 0
    y = 0 
    drawingBorder = True
    while drawingBorder:     
        text = hashFont.render("#" ,True,WHITE)
        teamName = hashFont.render("by SyntaxError", True, colorShift(WHITE), BACKGROUND_COLOR)

        WIN.blit(text,(x,y))
        WIN.blit(teamName,(WIDTH*0.6,0))
        #top line
        if(x < WIDTH and y == 0):
           x += XSpacing
        #right line
        elif(x >= WIDTH-XSpacing and y < HEIGHT-YSpacing):
            x = WIDTH - XSpacing
            y += YSpacing
        #bottom line
        elif(x > 0 and y >= HEIGHT - YSpacing):
            x -= XSpacing
        #left line
        elif(x <= 0 and y <= HEIGHT):
            y -= YSpacing
            if(y <= 0):
                drawingBorder = False
        
    if(welcome_screen):
        gameUi.gameTitle()
    
    if(welcome_screen):
        gameUi.welcomeScreen()
    elif(game_difficulty_screen):
        gameUi.gameDifficultyScreen(highlight)
    elif(gameplay_screen):
        print("main")
        gameUi.gameplayScreen()
        input.drawWord()
        input.drawuserInput(gameplayFont,input.startY)
        
        
        if(showHint):
            input.renderHint(word[1])

    updateScreen()
 


while game_running:
    pygame.time.Clock().tick(FPS)
    draw()
    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.display.quit()
            game_running = False
        elif(event.type == pygame.KEYDOWN):

            #change highlight for level selection
            if(event.key == pygame.K_UP):
                
                if(highlight > 0):
                    highlight -= 1
                
            elif(event.key == pygame.K_DOWN):
                if(highlight < 2):
                    highlight += 1
            #input event
            if(gameplay_screen and ((event.key >= 65 and event.key <= 90) or (event.key >= 97 and event.key <= 122)) and (len(input.keys) < input.missingLetterNumber)):
                input.userInput(chr(event.key))
                input.nextPosition()
                input.counter +=1
                if(input.cursorPos < len(input.missingPosition) -1):
                    input.cursorPos += 1

                
            #next event
            if(event.key == ENTER_KEY and gameplay_screen and (len(input.missingPosition) == len(input.keys))):
                if(lives > 0):
                    result = input.constructWord()
                    answer = word[0][1]
                    print(result,answer)
                    if(result == answer):
                        score += 10
                    else:
                        lives -= 1
                    print(lives,score)
                    #choose next word
                    
                    word = wordSplitter(level)
                    input.nextWord(word[0][1])
                    showHint = False
                else:
                    _score = Score()
                    _score.checkScore("time",score)
                    gameplay_screen = False
                    welcome_screen = False
                    game_difficulty_screen = False
                    leaderboard_Screen = True
            #delete event
            if(event.key == pygame.K_BACKSPACE and gameplay_screen):
                if(input.cursorPos > 0):
                   input.cursorPos -= 1
                input.deleteLetter()
            

            

            elif(event.key == pygame.K_ESCAPE and game_difficulty_screen == True):
                welcome_screen = True 
                gameplay_screen = False
                leaderboard_Screen = False
                game_difficulty_screen = False

            #quit the game if ESC is pressed and in welcome screen
            elif(event.key == pygame.K_ESCAPE and welcome_screen == True):
                pygame.display.quit()
                game_running = False

            #go to difficulty selection screen
            elif(event.key == ENTER_KEY and welcome_screen == True):
                welcome_screen = False
                game_difficulty_screen = True
                gameplay_screen = False
                leaderboard_Screen = True

            #show game play screen 
            elif(event.key == ENTER_KEY and game_difficulty_screen == True ):
                welcome_screen = False
                game_difficulty_screen = False
                gameplay_screen = True
                leaderboard_Screen = False
                level = levelList[highlight]
                word = wordSplitter(level)
                input = Input(word[0][1],WIN,startX,startY)             

            #show leader board if shift key is pressed 
            elif(event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT): 
                welcome_screen = False 
                gameplay_screen = False
                leaderboard_Screen = True
                game_difficulty_screen = False

            #this was the attempt at a quit screen because we did not want the user to accidentally escape the game
            elif(event.key == pygame.K_ESCAPE and gameplay_screen == True): 
                
                show_warning = True
                if(show_warning):
                    confirm = gameplayFont.render("Are you sure you want to quit?",True, RED)
                    WIN.blit(confirm, (WIDTH/2,HEIGHT/2))
                    updateScreen()
                   
            #show hint
            elif(event.key == pygame.K_TAB and gameplay_screen == True):
                showHint = True
                
                # warning screen
                
                #lose screen menu
                
                #view high scores screen


                
   
    
