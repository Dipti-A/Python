import timeit
import sys

#Set of Word list from dictionary
words = {"class", "case", "course", "dictionary", "java", "list", "program", "python", "tuple", "word"}

try:
    #Prompt user to enter letter and position
    letter = input("Enter the alphabet you want to find :")
    pos = input("Enter the position where you want to check the existence of the above alphabet :")

    #Iniatializing a set
    new_words = {""}

    #Function to check the occurence of given alphabet in given position
    def words_letter_position(w,l,p):
        i=0
        new_words.clear()
        #Using while loop
        for x in w:
            #Check that the requested position doesnt exceed the length of the word
            if p < len(x):
                if x[p] == l:
                    #If matches add to the newly created list
                    new_words.add(x)
            else:
                continue
        return w

    #Check that the position is numeric and letter is alphabet
    if(pos.isnumeric() and letter.isalpha()):
        w=words_letter_position(words,letter,int(pos))
        print("\noutput: result=", new_words)
    else:
        print("\nInvalid position or letter entered. Provide correct type")

    #Calculate execution time of the program
    execution_time = timeit.timeit()
    print("\nRuntime of the program :", execution_time)

except(Exception):
    e = sys.exc_info()[0]
    print("Error encountered : ", e)
    print("Try again...")
