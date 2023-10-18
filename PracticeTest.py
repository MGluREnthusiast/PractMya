### question 1

def doubler(x):
    return x*2

print(doubler(100))

### question 2

def countLowercase(string):
    k = 0
    for i in string:
        if i.islower():
            k += 1
    return k 

print(countLowercase("AeweadaSfaAFAFs"))

### question 3

def averagingColumns(Matrix):
    outputRow = []
    for i in range(len(Matrix[0])):
        outputRow.append(0)

    for i in range(len(Matrix)):
         for j in range(len(Matrix[i])):
                outputRow[j] += Matrix[i][j]/len(Matrix)
    ### also they call this operation a running mean. it solves the mean iteritvely instead of adding them dividing by the num of elements 
    ### this method is less computationally expensive then doing it through numpy or math modules because you would need to iteratively declare the columns

    return outputRow 
    ### you could also save len(10by10Matrix) as a variable and use it as I did, in fact this would be the computationally inexpensive soln

print(averagingColumns([[1, 3, 4, 4], [2, 5, 1, 4]]))

### question 4 

def KeepTHnames(listofNames):
    newList = []
    for i in listofNames:
        if i.find("th") != -1 or i.find("Th") != -1:
            ### .find() returns -1 if it does not find anything. This is typically not the case for most built in fxns for python as most will return an error so be careful
            newList.append(i)
    return newList

### question 5

def PigLatinToEnglish(pigLatin_phrase):
    num_Words =  pigLatin_phrase.count("ay")
    ayRemoved = pigLatin_phrase.replace("ay", "/")

    listof_words = []
    limit = 0
    for i in range(0, len(ayRemoved)):
        if ayRemoved[i] == "/":
                   ## this performs the shifting of the first letter to the last letter
                   listof_words.append(ayRemoved[i-1] + ayRemoved[limit:i-1])
                   limit = i+2
    
    return ' '.join(listof_words[0:])

print("PigLatin: ", PigLatinToEnglish("Iay atehay ouyay"))
