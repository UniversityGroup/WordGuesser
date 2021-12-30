import os

class Score:
    def __init__(self):
        #file whre score will be saved
        self.scoreFile = "scores.txt"
        #number of scores that can be saved
        self.maxScoreRecord = 10
        #create sore file if not exist
        self.checkFile()

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
    def checkScore(self):
        with open(self.scoreFile,"ra") as scores:
            lines = scores.readlines()
    
    
s = Score()
s.saveScore("sam",100)
s.saveScore("tim",90)
s.saveScore("jam",80)
s.saveScore("ram",70)
s.saveScore("pam",60)
s.saveScore("aim",50)
s.saveScore("bam",40)
s.saveScore("eam",30)
s.saveScore("uam",20)
s.saveScore("iim",10)


