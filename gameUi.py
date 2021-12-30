import pygame
from variables import *
from fonts import *
from main import WIN, updateScreen, age
from colors import *   

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
    question = textFont.render("How   old   are   you?",True, WHITE)
    enter = textFont.render("Enter your age",True,WHITE)
    prompt = controlsFont.render("press  ENTER  to  select / BACKPACE to delete / ESC to go back to main screen",True,WHITE)

    WIN.blit(question,(WIDTH/3, HEIGHT*0.65))
    WIN.blit(enter,(WIDTH/3, HEIGHT*0.75))
    WIN.blit(prompt, (WIDTH/4, HEIGHT*0.9))
    age.drawWord()
    age.drawuserInput(textFont, HEIGHT*0.74 )