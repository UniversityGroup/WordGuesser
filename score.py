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

    #create sore file if not exist
    def checkFile(self):
        if(not os.path.exists(self.scoreFile)):
            file = open(self.scoreFile, "w")
            file.close()

    #write score to a file
    def saveScore(self,name,score):
        with open(self.scoreFile, "a") as scores:
            scores.write(name+" "+str(score)+"\n")

    #check score and write from high to low 
    def checkScore(self,name, score):
        self.clone()
        with open(self.scoreFile,"r") as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                value = line.split(" ")[1]
                player = line.split(" ")[0]
                if(int(score) > int(value) and (player != name)):
                    print(player, name)
                    print("unique")
                    self.scores.insert(index, str(name)+ " " + str(score)+"\n")
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
        with open(self.scoreFile,"w") as file:
            for x in range(self.maxScoreRecord):
                print(x)
                file.write(array[x])





