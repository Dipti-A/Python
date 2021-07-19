from collections import defaultdict
from collections import deque
import sys

def PossibleAdjacents(words):
    adjList = defaultdict(list)
    graph = defaultdict(set)

    for word in words:
        for i in range(len(word)):
            # Removing a letter one by one
            possibleWords = word[:i]+"_"+ word[i+1:]
            adjList[possibleWords].append(word)
    # Add vertices and edges for words in the same graph
    for key, value in adjList.items():
        # For word1, word2
        for word1 in value:
            for word2 in value:
                if word1 != word2:
                    graph[word1].add(word2)
    return graph

# Remove eol character from each word in the list
def get_words(wordlist):
    for line in wordlist:
        yield line[:-1]

# Create graph based on Breadth first search(BFS) from start word
def BFS(graph, startWord, endWord):
    visitedNodes = set()
    queue = deque([[startWord]])

    while queue:
        path = queue.popleft()
        #Last element
        node = path[-1]
        yield node, path

        # Exclude already visited nodes from the graph
        nodesToTraverse = graph[node] - visitedNodes
        for n in nodesToTraverse:
            #Add the neighbours to already visited Nodes
            visitedNodes.add(n)
            #Add path along with the neigbour in the queue
            queue.append(path + [n])

if __name__ == '__main__':
    try:
        startWord = input("Enter the starting word :")
        endWord = input("Enter the end word :")

        # Read the given wordlist file
        wordlist = open("wordlist.txt", "r")
        wordGraph = PossibleAdjacents(get_words(wordlist))
        wordlist.close()

        bool = False

        # Print the shortest path using BFS search
        for node, path in BFS(wordGraph, startWord, endWord):
            #print("path....", path)
            if node == endWord:
                print(' -> '.join(path))
                bool = True

        if bool is False:
            print("Path not found between given words in the word ladder")

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
