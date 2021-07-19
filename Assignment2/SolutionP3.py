import random
import re
import sys

try:
    #Read random number from given file
    def random_word(fname):

        lines = open(fname).read().splitlines()
        randomWord = random.choice(lines)
        len(randomWord)
        print("I am thinking of a word that is", len(randomWord), "letters long! Try to guess this word!")
        return randomWord

    #Define variables,lists
    score=0
    correctGuess=0
    totalGuesses =5
    guessesLeft=5
    newWord=[]
    tmpList=[]
    listt=[]

    #Create new list object from random number from file
    listt=random_word('words.txt')

    #Create a new list with "-" values
    for count in range(len(listt)):
        newWord.insert(count,"-")

    #Guessing game begins...
    for i in range(totalGuesses):
        print("You have",guessesLeft,"guesses left!")
        if guessesLeft==0:
            break

        n = input("Please enter a letter:")
        guessesLeft -= 1

        if n in listt and n.isalpha():
            #Find all occurence of a letter in the given word
            pos = re.finditer(n, listt)
            pos = [i.start() for i in pos]
            tmpList=list(pos)
            correctGuess += 1
            print("good guess!")

            #Update the new list with the entered values
            for j in tmpList:
                newWord[j]=n
            print(newWord)
        else:
            print("Wrong guess!")
            print(newWord)

        if "-" not in newWord:
            print("You have No guesses left!")
            score = correctGuess * (i + 1)
            break
        else:
            score = correctGuess * (i + 1)
            continue

    #Now calculate the score
    finalScore=100+score

    finalWord=input("\nPlease enter the corresponding word: ")
    if finalWord == listt:
        print("You win! Your score is :",finalScore)
    else:
        print("Your score is :", score)
except:
    e = sys.exc_info()[0]
    print("Error encountered : ", e)
    print("Try again...")
