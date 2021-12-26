#resolution 
WIDTH, HEIGHT = 1200, 720
#control main while loop
game_running = True
# (#) border size
hashSize = 30
#setting frames per second
FPS = 60
#spacing for (#) border
XSpacing, YSpacing  = 20, 25
startX = WIDTH/3
startY = HEIGHT/3
#game screens
welcome_screen = False
gameplay_screen = True
leaderboard_Screen = False
game_difficulty_screen = False

#player score
score = 0
#player starting life
lives = 5
#difficulty level
level = "Intermediate"

#enter key
ENTER_KEY = 13