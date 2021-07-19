import sys

class Node:
    def __init__(self, data):
        self.dataVal = data
        self.nextVal = None

# Class representing a queue.The front stores the front node and rear stores the last node of Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue, where the insertion happens at the rear
    def enqueue(self, item):
        newItem = Node(item)

        # Inserting the first item in the queue
        if self.rear == None:
            self.front = newItem
            self.rear = newItem
            return

        # For inserting subsequent nodes in the queue
        self.rear.nextVal = newItem
        self.rear = newItem

    # Method to remove an item from queue, where the removal happens from the front
    def dequeue(self):
        # Return if the queue is empty
        if self.isEmpty():
            return

        # Changing the front node to the next Value after removing front node
        temp = self.front
        self.front = temp.nextVal

        # When last node is removed
        if (self.front == None):
            self.rear = None

    # Prints out the stack
    def printQueue(self):
        item = self.front
        if self.isEmpty():
            print("Queue is empty!")
        else:
            print("Queue is :")
            while (item != None):
                print(item.dataVal, "->", end=" ")
                item = item.nextVal
            return

class Stack:

    # Set head to null
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    # Method to add data to the stack. Its always added to the top of the stack
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.nextVal = self.head
            self.head = newNode

    # Remove element that is the current head i.e. top of the stack
    def pop(self):
        if self.isEmpty():
            print("Cannot pop any element as the stack is empty!")
            return None
        else:
            # Removes the head node and make the next one the new head
            removedNode = self.head
            self.head = self.head.nextVal
            removedNode.nextVal = None
            return removedNode.dataVal

    # Returns the head node data value
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.head.dataVal

    # Prints the stack
    def printStack(self):
        element = self.head
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print("\nStack is :")
            while (element != None):
                print(element.dataVal, "->", end=" ")
                element = element.nextVal
            return

if __name__ == '__main__':
    try:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.dequeue()
        q.dequeue()
        q.enqueue(3)
        q.enqueue(4)

        q.printQueue()

        s = Stack()

        s.push(11)
        s.push(22)
        s.push(33)
        s.push(33)
        s.push(55)

        # Delete top elements of stack
        s.pop()
        s.pop()

        # Display stack elements
        s.printStack()
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
