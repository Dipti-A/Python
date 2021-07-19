import sys

# Function to insert key values in the hashTable
def insert(hashTable, key, value):

    # In case key is string calculate the sum of ordinal values of all characters
    # and use this as the hashkey
    if str(key).isalpha():
        key = sum(ord(i) for i in key)

    # Use mod function to create hashkey
    hashKey = key % 7
    isKeyPresent = False

    # Retreive the existing list placed at ith position where i is the hashkey
    listt = hashTable[hashKey]
    # Iterate through the list of list
    for i, keyAndVal in enumerate(listt):
        k, v = keyAndVal
        if key == k:
            isKeyPresent = True
            break
    # Store the list of key value pair at the ith place in the list where i is the hashkey
    if isKeyPresent:
        listt[i] = ((key, value))
    else:
        listt.append((key, value))

# Method to search for a key in hashtable
def search(hashTable, key):
    # Calculate the sum of ordinal values of all characters
    if str(key).isalpha():
        key = sum(ord(i) for i in key)
    # Use mod function to create hashkey
    hashKey = key % 7

    # Iterate through the lists of list
    listt = hashTable[hashKey]
    for i, keyAndVal in enumerate(listt):
        k, v = keyAndVal
        if key == k:
            return v

if __name__ == '__main__':

    #Creating a list of list (nested lists)
    hashTable =[]
    cardinality = 7

    try:
        # Creating a list of sub-lists as per mentioned cardinality which will store the key values
        # inserted below at ith place where i is the hashkey calculated using mod function
        for x in range(cardinality):
            hashTable.append([])

        # Start inserting key values. Only int and string are allowed
        insert(hashTable,700, 700)
        insert(hashTable,21, 21)
        insert(hashTable,50, 50)
        insert(hashTable,85, 85)
        insert(hashTable,92, 92)
        insert(hashTable,101, 101)
        insert(hashTable,22, 22)
        insert(hashTable,23, 23)
        insert(hashTable,24, 24)
        insert(hashTable,25, 25)
        insert(hashTable,26, 26)
        insert(hashTable,28, 28)
        insert(hashTable,29, 29)
        insert(hashTable,29, 30)
        insert(hashTable,79, 79)
        insert(hashTable, 123, "Mary")
        insert(hashTable, "Cat", "Cat")
        insert(hashTable, "Human", "Mr. Peterson")
        insert(hashTable, "Car", 789)
        insert(hashTable, "Bike", "BMW")

        # Search for a particular key and result will be the corresponding value
        # In case key doesn't exist then value = None will be returned
        print(search(hashTable, 24))
        print(search(hashTable, 85))
        print(search(hashTable, 123))
        print(search(hashTable, "Human"))
        print(search(hashTable, "Car"))
        print(search(hashTable, "Bike"))

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
