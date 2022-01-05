#################################################By SynatxError#########################################################
# Author: Sandip Pradhan                                                                                               #
# This file is resposible for saving high score into a text file                                                       #
# functions:                                                                                                           #
#           CheckFile  - checks if score file exist, if not create one                                                 #
#           checkScore - Take a player score and calculates in which line it should be written in a scores file        #
#           writeFile  - Writes an array to scores file                                                                #
#           clone      - clones all the scores from scores file and copy it into scores array for some calculation     #
#                                                                                                                      #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################




import os


class Score:
    def __init__(self):
        #file whre score will be saved
        self.scoreFile = "scores.txt"
        #number of scores that can be saved
        self.maxScoreRecord = 10
        #create sore file if not exist
        self.checkFile()
        #scores array
        self.scores = []
        #if the score is lowest is the score leaderboard
        self.less = False

    #create score file if not exist
    def checkFile(self):
        if(not os.path.exists(self.scoreFile)):
            file = open(self.scoreFile, "w")
            file.close()


    #check score and write from high to low score in  file
    def checkScore(self,name, score):
        #clone the scores from scores.txt to an array
        self.clone()
        #player lsit in score file
        playerList = []
        #is player found in scores file
        isFound = False
        with open(self.scoreFile,"r") as file:
            lines = file.readlines()
            #if no player in score simply save it to file
            if(len(lines) < 1):
                self.scores.insert(0, str(name)+ " " + str(score)+"\n")
                self.writeFile(self.scores)
                self.scores = []
                return

            #loop through lines in scores file        
            for index, line in enumerate(lines):
                #get the score from line
                playerScore = line.split(" ")[1]
                #get the player name from line
                player = line.split(" ")[0]
                playerList.append(player)
                #if player exist
                if(name == player):
                    isFound = True
                    #only save score if it higher than last score
                    if(float(score) > float(playerScore)):
                        #remove player from score
                        self.scores.pop(index)
                        #check if the score updated is more than any other score on the list, if yes move the score to appropriate line.
                        for index, line in enumerate(lines):
                            #get the score from line
                            playerScore = line.split(" ")[1]
                            #get the player name from line
                            player = line.split(" ")[0]
                            if(float(score) > float(playerScore)):
                                # self.scores.pop(cloneIndex)
                                self.scores.insert(index, str(name)+ " " + str(score)+"\n")
                                self.writeFile(self.scores)
                                self.scores = []
                                return

                    self.writeFile(self.scores)
                    self.scores = []
                    isFound = False
                    return
            #if new player
            if(not isFound):
                #if the score is higher than any existing score append at top
                for index, line in enumerate(lines):
                    #get the score from line
                    playerScore = line.split(" ")[1]
                    #get the player name from line
                    player = line.split(" ")[0]
                    if(float(score) > float(playerScore)):
                        
                        self.scores.insert(index, str(name)+ " " + str(score)+"\n")
                        self.writeFile(self.scores)
                        self.scores = []
                        self.less = True
                        return
                        
            if(not self.less):
                #if the score is not higher than any existing code append at bottom
                for index, line in enumerate(lines):
                    #get the score from line
                    playerScore = line.split(" ")[1]
                    #get the player name from line
                    player = line.split(" ")[0]
                    if(float(score) < float(playerScore)):
                        self.scores.append(str(name)+ " " + str(score)+"\n")
                        self.writeFile(self.scores)
                        self.scores = []
                        return
                    
                        

            
    
    #clone the scores from scores.txt to an array
    def clone(self):
        with open(self.scoreFile,"r") as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                self.scores.insert(index, line)

    #write array to file
    def writeFile(self, array):
        if(len(array) < self.maxScoreRecord):
            self.maxScoreRecord = len(array)
        
        with open(self.scoreFile,"w") as file:
            for x in range(self.maxScoreRecord):
                file.write(array[x])






