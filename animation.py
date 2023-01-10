import pygame
import random
import time

alpha = 255
negative = False
positive = False
current_second = time.time()

def blink():
    global alpha, negative, positive
    if(alpha >= 255 and alpha > 0):
        positive = True
        negative = False
    elif(alpha <= 0):
        negative = True
        positive = False

    if(positive):
        alpha -= 5
    elif(negative):
        alpha += 5
    return alpha


def colorShift(color):
    return (random.randint(0,255),color[1],random.randint(0,255))


def onOff():
    global alpha
    global current_second

    if(alpha == 255 and int(time.time() - current_second) >= 3):
        alpha = 0
  
        current_second = time.time()
        
        return 0
    elif(alpha == 0 and int(time.time() - current_second) >= 3):
        alpha = 255

        current_second = time.time()
        return 255
    


    
    
    
