from collections import defaultdict
import timeit
import sys

try:
    #Read all words from txt file
    words_file = open("words.txt","r")
    lines = words_file.readlines()
    words_file.close()

    #Initializing variable and data structures
    dictL={}
    sortedWordDict={}
    croppedDict={}
    anagramDict={}
    tempDict={}
    newDict=[]

    n = int(input("Enter the number of letters for which all anagrams are required: "))

    #New dictionary with key as original word from file and value as sorted value of the same word
    for x in lines:
        # Convert to lower case and remove eol character
        str=x.rstrip('\n').lower()
        dictL[str]=sorted(str)

    #Filter out those elements which are not of given length n
    for x in dictL:
        if len(x) ==n:
            croppedDict.update({x:dictL[x]})

    #Function to find anagrams of given length
    def findAnagrams(sortedWordDict):
        for key in sortedWordDict:
            #Converted value from List to string
            listToStr = ''.join(sortedWordDict[key])
            tempDict[key]=listToStr

        anagramDict = defaultdict(list)
        for k, v in tempDict.items():
            anagramDict[v].append(k)

        #New list to hold the final list sorted by the count of the anagrams
        sortedList = []

        for x in anagramDict:
            num=len(anagramDict[x])
            if num>1:
                str = (num,anagramDict[x])
                sortedList.append(str)

        #Printing the final anagrams list
        for i in sorted(sortedList):
            print(i,'\n')

    #Invoke function to find anagrams of given length
    findAnagrams(croppedDict)

    #Calculate execution time of the program
    execution_time = timeit.timeit()
    print("Runtime of the program :", execution_time)

except:
    e = sys.exc_info()[0]
    print("Error encountered : ", e)
    print("Try again...")