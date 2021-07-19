import sys

# Method to find a duplicate element from list of sorted characters
def findNonDuplicate(A):
    # Return in case of empty list
    if len(A) == 0:
        print("\nInput list is empty. Enter valid input list!")
        return
    # Return in case of non-alphabetic characters present in list
    elif checkForSplChars(A):
        print("\nInvalid Input. Enter only alphabets or numeric characters in the input List!")
        return
    else:
        # Initializing the variables
        first=0
        last = len(A)-1
        uniqueElement=''

        if first > last:
            return uniqueElement

        if first == last:
            uniqueElement = A[first]
            return uniqueElement

        # Find the middle point
        midElement = int((last - first) / 2)

        # Using the divide and conquer approach where if middle element is even and same as the
        # next element then the non-duplicate character lies on the right side otherwise its on the left

        #If the middle position is even check the middle and the next element
        if midElement % 2 == 0:
            if A[midElement] == A[midElement + 1]:
                uniqueElement = findNonDuplicate(A[midElement+2:last+1])
            else:
                uniqueElement = findNonDuplicate(A[first:midElement+1])
        else:
            #If middle position is odd check the middle and the previous element
            if A[midElement] == A[midElement - 1]:
                uniqueElement = findNonDuplicate(A[midElement+1:last+1])
            else:
                uniqueElement = findNonDuplicate(A[first:midElement])

        return uniqueElement

# To check if the list contains any non-alphabetic characters
def checkForSplChars(A):
    for x in A:
        if type(x) == str:
            if not x.isalpha() :
                return True
    return False

if __name__ == "__main__":
    try:
        assert findNonDuplicate(['a','a','b','b','c','d','d','e','e','r','r']) == 'c'
        assert findNonDuplicate(['c','c','d','d','f','f','z']) == 'z'
    except AssertionError:
        print("\nThe required character is not a non-duplicate element. Try searching for a new character!")
    except NameError:
        print("\nName error occured. Error message: ",sys.exc_info()[1])
    except TypeError:
        print("\nType mismatch occured. Error message: ",sys.exc_info()[1])
    except ValueError:
        print("\nValue error occurred. Error message: ",sys.exc_info()[1])
    except IndexError:
        print("\nIndex error occurred. Error message: ",sys.exc_info()[1])
    except SyntaxError:
        print("\nSyntax error ocurred. Error message: ",sys.exc_info()[1])
    except AttributeError:
        print("\nAttribute error occured. Error message: ",sys.exc_info()[1])
    except Exception:
        print("Error encountered : ", sys.exc_info()[0])
        print("Try again...")
