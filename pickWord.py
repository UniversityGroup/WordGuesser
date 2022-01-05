import random

class PickWord:
    def __init__(self, level):
        self.FILE = "word_list.txt"
        self.level = level
        #word line range for beginner difficuly in word_list file
        self.easy = []
        #word line range for intermediate difficuly in word_list file
        self.medium = []
        #word line range for expert difficuly in word_list file
        self.hard = []
        self.getWordDifficulty()



    #read the word_list file and get the line number range for each difficulty level
    def getWordDifficulty(self):
        count = 1
        with open(self.FILE) as file:
            for line in file.readlines():
                if("Easy" in line):
                    self.easy.append(count+1)
                elif("Medium" in line):
                    self.easy.append(count-1)
                    self.medium.append(count+1)
                elif("Hard" in line):
                    self.medium.append(count-1)
                    self.hard.append(count+1)
                count += 1
            self.hard.append(count-1)



    #pick a random line given a difficulty level
    def getWord(self):
        if(self.level == "Easy"):
            #pick a random line form beginner[] range
            randomLine = random.randint(self.easy[0]-1,self.easy[1]-1)
            with open(self.FILE) as file:
                #split the line where - is
                result = file.readlines()[randomLine]
                print("random line ",randomLine)
                print("random line result ",result)
                result = result.split("-")
                print("this line is ", str(result))
                
                #remove any white space and return the result
                return [result[0].strip(), result[1].strip()]
        elif(self.level == "Medium"):
            #pick a random line form beginner[] range
            randomLine = random.randint(self.medium[0]-1,self.medium[1]-1)
            print("medium, picking line: ",randomLine)
            with open(self.FILE) as file:
                #split the line where - is
                result = file.readlines()[randomLine].split("-")
                #remove any white space and return the result
                return [result[0].strip(), result[1].strip()]
        elif(self.level == "Hard"):
            #pick a random line form beginner[] range
            randomLine = random.randint(self.hard[0]-1,self.hard[1]-1)
            with open(self.FILE) as file:
                #split the line where - is
                result = file.readlines()[randomLine].split("-")
                #remove any white space and return the result
                return [result[0].strip(), result[1].strip()]

        



