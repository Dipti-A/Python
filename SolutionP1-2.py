import timeit
import sys

#List of Word from dictionary
words = ["class", "case", "course", "dictionary", "java", "list", "program", "python", "tuple", "word"]

try:
    #Prompt user to enter letter and position
    letter = input("Enter the alphabet you want to find :")
    pos = input("Enter the position where you want to check the existence of the above alphabet :")

    #Initializing a list
    new_words = []

    #Function to check the occurence of given alphabet in given position
    def words_letter_position(w,l,p):
        #Iterating thru all the elements of list
        for x in w:
            #Check that the requested position doesnt exceed the length of the word
            if p < len(x):
                if x[p] == l:
                    #If matches add to the newly created list
                    new_words.append(x)
            else:
                continue
        return w

    #Check that the position is numeric and letter is alphabet
    if(pos.isnumeric() and letter.isalpha()):
        w=words_letter_position(words,letter,int(pos))
        print("\noutput: result", new_words)
    else:
        print("\nInvalid position or letter entered. Provide correct type")

    #Calculate execution time of the program
    execution_time = timeit.timeit()
    print("\nRuntime of the program :", execution_time)

except:
    e = sys.exc_info()[0]
    print("Error encountered : ", e)
    print("Try again...")