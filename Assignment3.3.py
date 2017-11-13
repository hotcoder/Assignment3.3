'''
Finding longest word from the list of words
'''

'''
input : listOfWords
output : longest length word
'''
def longestWord(listOfWords):
    maxLength=-1
    maxLengthWord=''
    for word in listOfWords:
        if(len(word) >= maxLength):
            maxLength = len(word)
            maxLengthWord=word
    return maxLengthWord


listOfWords = ["abc",'asas','qwqwa']

print(longestWord(listOfWords))

