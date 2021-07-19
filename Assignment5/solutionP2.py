import sys

#Palindrome implementation using stack
class Stack:
    #Initialise a list
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # Method to add an item to the stack, where the insertion happens from top
    def push(self, data):
        self.items.append(data)

    # Method to remove an item from the stack, where the removal also happens from top
    def pop(self):
        return self.items.pop()

    #Method to check if the given string is a Palindrome using stack implementation
    def isPalindrome(stk, str):

        length = len(str)
        # Finding the mid as the stack capacity is half of the length of entered string rounded down
        mid = length // 2
        i = 0

        # Pushing only half of the elements in stack due to above restriction
        while i < mid:
            stk.push(str[i])
            i += 1

        # If the length of the string is odd then skip the middle element
        if length % 2 != 0:
            i += 1

        # Pop elements from stack and compare with the ith element from string one by one
        while i < length:
            item = stk.pop()
            st = "".join(item)
            # Ignoring case sensitivity
            if st.lower() != str[i].lower():
                # If any character differs then the given string is not a palindrome
                return False
            i += 1
        # If none of the characters differ then the given string is a palindrome
        return True

#Palindrome implementation using queue
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # Method to add an item to the queue, where the insertion happens at the end
    def enqueue(self, item):
        self.items.append(item)

    # Method to remove an item from queue, where the removal happens from the front
    def dequeue(self):
        return self.items.pop(0)

    # Method to check if the given string is a Palindrome using Queue implementation
    def isPalindrome(q, str):

        length = len(str)
        # Finding the mid as the queue capacity is half of the length of entered string rounded up
        mid = length // 2
        i = 0

        # Pushing only half of the elements in stack due to above restriction
        while i < mid+1:
            q.enqueue(str[i])
            i += 1

        # If the length of the string is odd then skip the middle element
        if length % 2 != 0:
            i += 1

        # Pop elements from top of the queue and compare with the last element from string
        while i < length:
            item = q.dequeue()
            st = "".join(item)
            # Ignoring case sensitivity
            if st.lower() != str[length-1].lower():
                # If any character differs then the given string is not a palindrome
                return False
            length -= 1
        # If none of the characters differ then the given string is a palindrome
        return True

def ignoreSplChars(text):
    # Ignoring all white spaces between the entered string
    text = text.replace(" ", "")

    # Ignoring all punctations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Traverse the given string and if any punctuation marks occur replace it with null
    for i in text.lower():
        if i in punctuations:
            text = text.replace(i, "")

    return text

if __name__ == '__main__':
    try:
        s = Stack()
        text = input('Please enter the string: ')

        text = ignoreSplChars(text)
        # Check if the input string is empty
        if len(text) == 0:
            print("Input string is empty. Please enter valid string value!")
        else:
            #Checking if the entered string is a palindrome using stack implementation
            if s.isPalindrome(text):
                print('The string is a palindrome.')
            else:
                print('The string is not a palindrome.')

            #Implementation using queue
            q=Queue()
            if q.isPalindrome(text):
                print('The string is a palindrome.')
            else:
                print('The string is not a palindrome.')
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

