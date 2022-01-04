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


from pygame.mixer import pause
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
pygame.display.set_caption("WordGuesser")
word = None
input = None

gameUi = Ui(WIN)
#highlight for level selection 
highlight = 0
#highlight for warning screen
warningHighlight = 0
#Player name input for the game over screen
name = Input(["_","_","_"],WIN,WIDTH*0.2,HEIGHT*0.5)

#load sound effect
sound = pygame.mixer.Sound("vgmenuhighlight.wav")
#load music 
pygame.mixer.music.load("game_music.mp3")



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
        gameUi.gameplayScreen(level,lives,score,skips)
        input.drawWord()
        input.drawuserInput(gameplayFont,input.startY)
        #show hint
        if(showHint):
            input.renderHint(word[1])
    elif(leaderboard_Screen):
        gameUi.leaderboardScreen()
    elif(game_over_screen):
        #draw game over screen
        gameUi.gameOverScreen(score)
        #draw the inputbox
        name.drawWord()
        #draw user input
        name.drawuserInput(textFont,HEIGHT*0.5)
    elif(warning_screen):
        gameUi.warningScreen(warningHighlight)
    elif(show_result):
        gameUi.showResult(word[0][0],input.constructWord(),level,lives,score)

    updateScreen()
 
    

while game_running:
    #set Frams per second
    pygame.time.Clock().tick(FPS)
    #draw objects
    draw()
    #play music
    if(music_on and not is_music_playing and not paused):
        pygame.mixer.music.play(-1)
        is_music_playing = True
    elif(not music_on and is_music_playing):
        pygame.mixer.music.pause()
        is_music_playing = False
        paused = True
    elif(music_on and paused and not is_music_playing):
        paused = False
        is_music_playing = True
        pygame.mixer.music.unpause()

  
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.display.quit()
            game_running = False
        elif(event.type == pygame.KEYDOWN):
            #play sound
            if(sound_on):
                sound.play()
            

            #toggle sound
            if(event.key == pygame.K_LCTRL):
                sound_on = not sound_on

            #toggle music
            if(event.key == pygame.K_RCTRL):
                music_on = not music_on


            #change highlight for level selection
            if(event.key == pygame.K_UP and game_difficulty_screen):
                
                if(highlight > 0):
                    highlight -= 1
                
            elif(event.key == pygame.K_DOWN and game_difficulty_screen):
                if(highlight < 2):
                    highlight += 1

            
            #warning screen option selection
            if(warning_screen and event.key == pygame.K_RIGHT):
                if(warningHighlight < 1):
                    warningHighlight += 1
            elif(warning_screen and event.key == pygame.K_LEFT):
                if(warningHighlight > 0):
                    warningHighlight -= 1

            #handle event when enter key is pressed in warning screen
            if(warning_screen and event.key == ENTER_KEY):
                if(warningHighlight == 0):
                    warning_screen = False
                    gameplay_screen = True
                elif(warningHighlight == 1):
                    warning_screen = False
                    welcome_screen = True


            #gameover input event/get playername
            if(game_over_screen and len(name.keys) < name.missingLetterNumber and ((event.key >= 65 and event.key <= 90) or (event.key >= 97 and event.key <= 122))):
                name.userInput(chr(event.key))
                name.nextPosition()
                name.counter += 1
                if(name.cursorPos < len(name.missingPosition)-1):
                    name.cursorPos += 1
            if(game_over_screen and event.key == pygame.K_BACKSPACE):
                if(name.cursorPos > 0):
                    name.cursorPos -= 1
                if(name.counter > 0):
                    name.deleteLetter()


            
            #input event
            if(gameplay_screen and ((event.key >= 65 and event.key <= 90) or (event.key >= 97 and event.key <= 122)) and (len(input.keys) < input.missingLetterNumber)):

                input.userInput(chr(event.key))
                input.nextPosition()
                input.counter +=1
                if(input.cursorPos < len(input.missingPosition) -1):
                    input.cursorPos += 1

                
            #next puzzle
            if(event.key == ENTER_KEY and gameplay_screen and (len(input.missingPosition) == len(input.keys))):
                show_result = True
                gameplay_screen = False
                
            
            elif(show_result and event.key == ENTER_KEY):
                show_result = False
                gameplay_screen = True
                if(lives > 1):
                    result = input.constructWord()
                    answer = word[0][0]
                    result[0] = result[0].upper()
                    answer[0] = answer[0].upper()
                    print("###############",answer,result)
                    if(result == answer):
                        print(result,answer)
                        score += 10
                    else:
                        lives -= 1
                    
                    #choose next random word
                    
                    word = wordSplitter(level)
                    input.nextWord(word[0][1])
                    showHint = False
                else:
                    gameplay_screen = False
                    welcome_screen = False
                    game_difficulty_screen = False
                    game_over_screen = True
                    leaderboard_Screen = False
                    #if game overscreen and name was entered save score
                    
            if(game_over_screen and event.key == ENTER_KEY):
                #only save if name is entered
                if(len(name.constructString()) > 0):
                    print(name.constructString())
                    _score = Score()
                    _score.checkScore(name.constructString(),score)
                    # game_over_screen = False
                    # leaderboard_Screen = True
                        
            #skip if \ is pressed
            elif(gameplay_screen and event.key == pygame.K_BACKSLASH and skips > 0):
                show_result = False
                gameplay_screen = True
                skips -= 1
                if(lives > 0):
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
                    game_over_screen = True
                    leaderboard_Screen = False

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
            elif((event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) and welcome_screen): 
                welcome_screen = False 
                gameplay_screen = False
                leaderboard_Screen = True
                game_difficulty_screen = False

            #this was the attempt at a quit screen because we did not want the user to accidentally escape the game
            elif(event.key == pygame.K_ESCAPE and gameplay_screen == True): 
                gameplay_screen = False
                warning_screen = True
                
                   
            #show hint
            elif(event.key == pygame.K_TAB and gameplay_screen == True):
                showHint = True
                
            
            elif(leaderboard_Screen and event.key == pygame.K_ESCAPE):
                leaderboard_Screen = False
                welcome_screen = True
                
           


                
   
    
