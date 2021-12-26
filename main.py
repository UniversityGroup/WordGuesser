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
from inputSystem import InputSystem
from input import Input
from wordSplitter import wordSplitter




#Game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Game window title
pygame.display.set_caption("Render")

word = wordSplitter()
input = Input(word[1],WIN,startX,startY)

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
        
    if(not gameplay_screen):
        gameTitle()
    
    if(welcome_screen):
        welcomeScreen()
    elif(game_difficulty_screen):
        gameDifficultyScreen()
    elif(gameplay_screen):
        input.drawWord()
        input.drawuserInput()

    updateScreen()
    
def welcomeScreen():
        controls = textFont.render("press   ENTER   top  play   or  ESC  to quit", True, WHITE)
        controls2 = textFont.render("press  SHIFT   for    leaderboard", True, WHITE)
        controls2.set_alpha(blink())
        controls.set_alpha(blink())
        WIN.blit(controls, (WIDTH/4,HEIGHT*0.6))
        WIN.blit(controls2, (WIDTH/4,HEIGHT*0.68))
        updateScreen()
        

def gameTitle():
        W = titleFont.render("W",True, WHITE)
        ORD = titleFontOut.render("ORD",True, WHITE)
        G = titleFont.render("G",True, WHITE)
        UESSER = titleFontOut.render("UESSER",True, WHITE)
        WIN.blit(W,(WIDTH/3,HEIGHT/8))
        WIN.blit(G,(WIDTH/3+100,HEIGHT/3))
        WIN.blit(ORD, (WIDTH/3+100, HEIGHT/8))
        WIN.blit(UESSER, (WIDTH/3+180, HEIGHT/3))

def gameDifficultyScreen():
    age = textFont.render("How   old   are   you?",True, WHITE)
    enter = textFont.render("Enter your age ___",True,WHITE)
    prompt = controlsFont.render("press  ENTER  to  select / BACKPACE to delete / ESC to go back to main screen",True,WHITE)

    WIN.blit(age,(WIDTH/3, HEIGHT*0.65))
    WIN.blit(enter,(WIDTH/3, HEIGHT*0.75))
    WIN.blit(prompt, (WIDTH/4, HEIGHT*0.9))



while game_running:
    pygame.time.Clock().tick(FPS)
    draw()
    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.display.quit()
            game_running = False
        elif(event.type == pygame.KEYDOWN):
            #input event
            if(gameplay_screen and (event.key >= 65 and event.key <= 90) or (event.key >= 97 and event.key <= 122) and (len(input.keys) < input.missingLetterNumber)):
                input.userInput(chr(event.key))
                input.nextPosition()
                input.counter +=1
                if(input.cursorPos < len(input.missingPosition) -1):
                    input.cursorPos += 1
                    print("main counter",input.counter)
                    
                    
                
                
                
            #next event
            if(event.key == ENTER_KEY and gameplay_screen):
                if(lives > 0):
                    result = input.constructWord()
                    answer = word[0]
                    if(result == answer):
                        score += 10
                    else:
                        lives -= 1
                    #choose next word
                    word = wordSplitter()
                    input.nextWord(word[1])
                else:
                    gameplay_screen = False
                    welcome_screen = True
                

            #delete event
            if(event.key == pygame.K_BACKSPACE and gameplay_screen):
               
                if(input.cursorPos > 0):
                   input.cursorPos -= 1
            
                input.deleteLetter()

            #choose next puzzle
            if(event.key == ENTER_KEY and (len(input.missingLetters) == len(input.keys))):
                input.nextWord(word[1])
            elif(event.key == pygame.K_ESCAPE and game_difficulty_screen == True):
                welcome_screen = True 
                gameplay_screen = False
                leaderboard_Screen = False
                game_difficulty_screen = False

            elif(event.key == pygame.K_ESCAPE and welcome_screen == True):
                pygame.display.quit()
                game_running = False

            elif(event.key == ENTER_KEY and welcome_screen == True):
                welcome_screen = False
                game_difficulty_screen = True
                gameplay_screen = False
                leaderboard_Screen = True

            elif(event.key == ENTER_KEY and game_difficulty_screen == True ):
                welcome_screen = False
                game_difficulty_screen = False
                gameplay_screen = True
                leaderboard_Screen = False                

            elif(event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT): #see pygame library for different buttons 
                welcome_screen = False 
                gameplay_screen = False
                leaderboard_Screen = True
                game_difficulty_screen = False

            elif(event.key == pygame.K_ESCAPE and gameplay_screen == True): #this was the attempt at a quit screen because we did not want the user to accidentally escape the game
                print(show_warning)
                show_warning = True
                if(show_warning):
                    confirm = gameplayFont.render("Are you sure you want to quit?",True, RED)
                    WIN.blit(confirm, (WIDTH/2,HEIGHT/2))
                    updateScreen()
                   


                
   
    
