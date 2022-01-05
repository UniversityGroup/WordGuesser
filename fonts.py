########################################################By SynatxError###########################################
# Author: Sandip pradhan - 24899810
# This file contains font data
##################################################################################################################

import pygame
from variables import *
#initialise fonts
pygame.font.init()
#Fonts
textFont = pygame.font.Font("./fonts/a-note.regular.ttf",40, bold =False, italic=True)
gameplayFont = pygame.font.Font("./fonts/a-note.regular.ttf",80, bold =False, italic=True)
controlsFont = pygame.font.Font("./fonts/a-note.regular.ttf",20, bold =False, italic=True)
hashFont = pygame.font.Font("./fonts/Shaky Hand Some Comic.otf", hashSize, bold=False, italic=False)
teamFont = pygame.font.SysFont("Courier 10 Pitch", 40, bold=True, italic=True)
titleFont = pygame.font.Font("./fonts/Shaky Hand Some Comic.otf", 150, bold=False, italic=False)
titleFontOut = pygame.font.Font("./fonts/Shaky Hand Some Comic_3D.otf", 150, bold=False, italic=False)
