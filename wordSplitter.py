#assume you have a word
import random
import time
from variables import level
from pickWord import PickWord

wordPicker = PickWord(level)



def less_Code(length,array,missing):
    already_choosen = []
    original_array = array.copy()
    missing_length = int(length*0.6)
    while len(already_choosen) < missing_length:
        random_position = random.randrange(length-1)
        if(random_position not in already_choosen):
            already_choosen.append(random_position)
            missing.append(array[random_position])
            array[random_position] = "_"
    return [original_array, array]






def wordSplitter():  #catcatcat1
    line = wordPicker.getWord()
    hint = line[1]
    word = line[0]
    print(word,hint)
    length = len(word)
    array = list(word)  # [c,a,t,c,a,t,c,a,t,1]
    missing = []
    result = []
    missing_word = ""
    for x in range(length):
        missing.append("_")
    if length <= 10:
        result = less_Code(length,array,missing)
    else:
        result = less_Code(length,array,missing) # makes the code work if it's not exactly 10 letters

    for x in result:
        if x == 0:
            missing_word += "_"
        else:
            missing_word += str(x)
    
    return result



# wordSplitter() 
