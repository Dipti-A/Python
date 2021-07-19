import sys

#Generator to yield the string values one by one
def generator(st):
    for i in st:
        yield(i)

def encode(st):
    count=1
    l = []
    pos=0
    try:
        myGen = generator(st)
        for i in st:
            currVal=next(myGen)
            nextVal=next(myGen)
            if currVal == nextVal:
                if currVal in l:
                    #finding last occurence of current value using slice + index
                    pos = len(l) - 1 - l[::-1].index(currVal)
                    if l[pos]==l[len(l)-2]:
                        l[pos + 1] = int(l[pos + 1]) + count * 2
                    else:
                        l.append(currVal)
                        l.append(count*2)
                    #Reset counter to 1 and current and next values
                    count=1
                    currVal=''
                else:
                    #Counting both currentValue and nextValue
                    count *= 2
                    l.append(currVal)
                    l.append(str(count))
                    #Reset counter to 1 and current value
                    count=1
                    currVal = ''

            elif currVal != nextVal:
                #Finding last occurence of current value using slice + index
                if currVal in l:
                    pos = len(l) - 1 - l[::-1].index(currVal)
                    if l[pos] == l[len(l) - 2]:
                        l[pos + 1] = int(l[pos + 1]) + count
                    else:
                        l.append(currVal)
                        l.append(str(count))
                else:
                    #Adding current value
                    l.append(currVal)
                    l.append(str(count))
                #Adding nextValue as well
                l.append(nextVal)
                l.append(str(count))
                #Reset counter and current value
                count=1
                currVal = ''

    except StopIteration:
        #Adding current item when next item does not exist and iteration stopped
        if currVal != '':
            if currVal in l:
                pos = len(l) - 1 - l[::-1].index(currVal)
                if l[pos]==l[len(l)-2]:
                    l[pos+1]=int(l[pos+1])+count
                else:
                    l.append(currVal)
                    l.append(str(count))
            else:
                l.append(currVal)
                l.append(str(count))
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

    # Converting the dictionary into concatenated string
    encodedStr = ''.join((str(j)) for j in l)
    print("\nEncoded value of", st, "is :", str(encodedStr))

def decode(st):
    l=[]
    try:
        myGen = generator(st)
        for i in st:
            currVal = next(myGen)
            nextVal = next(myGen)
            for j in range(int(nextVal)):
                l.append(currVal)
    except StopIteration:
        #Converting resultant list into string
        res=""
        for ele in l:
            res = res + str(ele)
        print("\nDecoded value of",st,"is :", res)
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

#Specify string to encode
strToEncode="bbccccccdrrrffhhhh"
encode(strToEncode)

#Specify string to decode
strToDecode="b2c6d1r3f2h4"
decode(strToDecode)