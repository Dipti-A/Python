import operator
import sys
from functools import reduce

def multiMerge(ListOfArrays):
    if len(ListOfArrays) > 0:
        arr =[]
        dict={}
        isNumeric=False

        # Converting into a single list
        arr = reduce(operator.concat,ListOfArrays)
        # Remove duplicate elements
        arr = mergeList(arr)
        """dict = dict.fromkeys(arr)

        # Check for non-numeric characters
        for i in dict.keys():
            if str(i).isnumeric():
                isNumeric = True
            else:
                isNumeric = False
                print("\nThe List of array contains non-numeric values. Try again with valid numeric data!")
                break
        if isNumeric:
            arr = list(dict)
            arr = mergeList(arr)
        """
        return arr
    else:
        print("\nInput list is empty. Enter valid input list!")

def mergeList(arr):
# Given an input  k sorted lists of size n each we need to return a sorted list of kn elements
# by using recursion

    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2

        leftArr = arr[:mid]
        rightArr = arr[mid:]

        # Sorting the first half
        mergeList(leftArr)
        # Sorting the second half
        mergeList(rightArr)

        i = j = k = 0
        print("LeftArr and rightArr values are....", leftArr, rightArr)
        # Comparing and merging the elements in case of single elements
        while i < len(leftArr) and j < len(rightArr):
            print("i,j,k are ----->>", i,j,k)
            print("leftArr[i] and rightArr[j] values are +++++++++++++", leftArr[i],rightArr[j])
            # In case of duplicates dont add to the temp list
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                print("arr[k] value is ************", arr[k])
                i += 1
                k+=1

            elif leftArr[i] > rightArr[j]:
                arr[k] = rightArr[j]
                print("arr[k] value is ************", arr[k])
                j += 1
                k+=1

            elif leftArr[i] == rightArr[j]:
                print("duplicates values are there....", leftArr[i])
                j += 1

        # Checking if any element was left
        while i < len(leftArr):
            print("inside new while=======")
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
    #print("Sorted list is ----->", arr)
    return arr

if __name__ == "__main__":
    try:
        assert multiMerge([[1,3,5],[2,7,9],[0,6,8]]) == [0, 1, 2, 3, 5, 6, 7, 8, 9]
        #arr= [[1,1,3,5],[2,7,7,9],[0,6,8,10],[11,20,7,2],[1,19,4,'a']]

    except AssertionError:
        print("\nThe required list is not the sorted version for the input list. Try again!")
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

