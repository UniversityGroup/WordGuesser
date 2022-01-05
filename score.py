import os
from math import floor

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
                cloneIndex = index
                print("intial clone is ",self.scores)
                #if player exist
                if(name == player):
                    print("index ", index)
                    print("player ",name," is in playeList ",playerList)
                    isFound = True
                    #only save score if it higher than last score
                    if(float(score) > float(playerScore)):
                        self.scores[index] = str(name)+ " " + str(score)+"\n"
                        for index, line in enumerate(lines):
                            #get the score from line
                            playerScore = line.split(" ")[1]
                            #get the player name from line
                            player = line.split(" ")[0]
                            if(float(score) > float(playerScore)):
                                self.scores.pop(cloneIndex)
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
                print("11111111")
                #if the score is higher than any existing score append at top
                for index, line in enumerate(lines):
                    #get the score from line
                    playerScore = line.split(" ")[1]
                    #get the player name from line
                    player = line.split(" ")[0]
                    print(playerScore, score)
                    if(float(score) > float(playerScore)):
                        print("unique")
                        self.scores.insert(index, str(name)+ " " + str(score)+"\n")
                        self.writeFile(self.scores)
                        self.scores = []
                        return
                        
            if(not isFound):
                print("222222222")     
                #if the score is not higher than any existing code append at bottom
                for index, line in enumerate(lines):
                    #get the score from line
                    playerScore = line.split(" ")[1]
                    #get the player name from line
                    player = line.split(" ")[0]
                    print(playerScore, score)
                    if(float(score) > float(playerScore)):
                        print("unique2")
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
                print(x)
                file.write(array[x])


    
