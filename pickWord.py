import random

class PickWord:
    def __init__(self, level):
        self.FILE = "word_list.txt"
        self.level = level
        #word line range for beginner difficuly in word_list file
        self.beginner = []
        #word line range for intermediate difficuly in word_list file
        self.intermediate = []
        #word line range for expert difficuly in word_list file
        self.expert = []
        self.getWordDifficulty()



    #read the word_list file and get the line number range for each difficulty level
    def getWordDifficulty(self):
        count = 1
        with open(self.FILE) as file:
            for line in file.readlines():
                if("Beginner" in line):
                    self.beginner.append(count+1)
                elif("Intermediate" in line):
                    self.beginner.append(count-1)
                    self.intermediate.append(count+1)
                elif("Expert" in line):
                    self.intermediate.append(count-1)
                    self.expert.append(count+1)
                count += 1
            self.expert.append(count-1)


    #pick a random line given a difficulty level
    def getWord(self):
        if(self.level == "Beginner"):
            #pick a random line form beginner[] range
            randomLine = random.randint(self.beginner[0],self.beginner[1])
            with open(self.FILE) as file:
                #split the line where - is
                result = file.readlines()[randomLine].split("-")
                #remove any white space and return the result
                return [result[0].strip(), result[1].strip()]
        elif(self.level == "Intermediate"):
            #pick a random line form beginner[] range
            randomLine = random.randint(self.intermediate[0],self.intermediate[1])
            with open(self.FILE) as file:
                #split the line where - is
                result = file.readlines()[randomLine].split("-")
                #remove any white space and return the result
                return [result[0].strip(), result[1].strip()]
        elif(self.level == "Expert"):
            #pick a random line form beginner[] range
            randomLine = random.randint(self.expert[0],self.expert[1])
            with open(self.FILE) as file:
                #split the line where - is
                result = file.readlines()[randomLine].split("-")
                #remove any white space and return the result
                return [result[0].strip(), result[1].strip()]



