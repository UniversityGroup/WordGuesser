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
welcome_screen = True
gameplay_screen = False
leaderboard_Screen = False
game_difficulty_screen = False
game_over_screen = False
warning_screen = False
show_result = False

#player score
score = 0
#player starting life
lives = 5
#difficulty level
levelList = ["Easy","Medium","Hard"]
level = "Easy"
#skips available to player
skips = 5

#show hint
showHint = False

#enter key
ENTER_KEY = 13