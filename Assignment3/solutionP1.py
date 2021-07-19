import random
import sys

class CardGame():
    #class variable
    listOfCards=[]

    def __init__(self):
        l=self.listOfCards
        #Value of numbers from 2 to 14 and Value of shape 0 to 3
        for number in range(2,15):
            for shape in range(0,4):
                tup=(number,shape)
                l.append(tup)

    #Function to generate card name in specific format
    def card_name(self,number, shape):
        #Create dictionary to hold numbers and shapes of the cards
        numDict={2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'Jack',12:'Queen',13:'King',14:'Ace'}
        shapeDict={0:'Hearts', 1:'Diamonds', 2:'Clubs', 3:'Spades'}
        if number in numDict:
            cardName= numDict[number]
        if shape in shapeDict:
            cardShape= shapeDict[shape]

        cardName= cardName +" of "+cardShape
        return cardName

    #Function to randomly shuffle the tuples
    def shuffling(self):
        l=self.listOfCards
        totalCards=52
        #Create a new list after shuffling
        newShuffledlist= random.sample(l,totalCards)
        return newShuffledlist

    #Function to remove the tuple from the list
    def draw(self,tup,llist):
        if tup in llist and len(llist)>0:
            llist.remove(tup)
        if len(llist)==0:
            llist.append("None")
        return llist

    def __str__(self):
        pass

try:
    # Instantiating a CardGame object for both players A and B
    A = CardGame()
    B = CardGame()

    # Initialising scores for both the players
    scoreA = 0
    scoreB = 0
    numOfCards = 52

    #Shuffle both the decks A and B before starting the game
    listA=A.shuffling()
    listB=B.shuffling()

    print("Player A Vs Player B :")
    i=0
    while i < numOfCards and len(listA)>0 and len(listB)>0:
        if (listA[i] == "None" and listB[i] == "None"):
            break;
        if listA[i] == listB[i]:
            pass
        elif listA[i]>listB[i]:
            scoreA+=1
        elif listB[i]>listA[i]:
            scoreB+=1

        #Invoke card_name by passing number and shape for both cards
        cardNameA= A.card_name(listA[i][0], listA[i][1])
        cardNameB= B.card_name(listB[i][0], listB[i][1])

        cardName=cardNameA+" * "+cardNameB+" ==> Points: "+str(scoreA)+" * "+str(scoreB)
        print(cardName)

        ACard = A.draw(listA[i],listA)
        BCard = B.draw(listB[i],listB)
    i+=1

    print("Player A has",scoreA,"points",",Player B has",scoreB,".")
    if scoreB>scoreA:
        print("Winner is: Player B")
    elif scoreB==scoreA:
        print("Its a Draw!")
    else:
        print("Winner is: Player A")
except NameError:
    print("\nName error occured.. Try again!")
except TypeError:
    print("\nType mismatch occured.. Try again!")
except ValueError:
    print("\nValue error occurred.. Try again! ")
except IndexError:
    print("\nIndex error occurred.. Try again!")
except SyntaxError:
    print("\nSyntax error ocurred.. Try again!")
except AttributeError:
    print("\nAttribute error occured. Try again")
except Exception:
    e = sys.exc_info()[0]
    print("Error encountered : ", e)
    print("Try again...")
