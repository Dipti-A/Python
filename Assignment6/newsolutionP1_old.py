
from queue import Queue
from collections import deque

class Doublet:

    def generateAdjList(self, wordList):
        adj = {}
        for w in wordList:
            for i in range(len(w)):
                key = w[:i]+"*"+ w[i+1:]
                adj[key]=adj.get(key,[])
                adj[key].append(w)
            #print("adjacency list is -", adj)
        return adj

    """def wordlenth(self, startWord, endWord, wordList):
        set = wordList

        if endWord not in set:
           return 0

        q = Queue()
        q.put(startWord)
        visited=[]

        changes = 1
        while not(q.empty()):
            size = q.qsize()
            for i in range(size):
                word = q.get()
                if word == endWord:
                    return changes

                for j in range(len(word)):
                    k='a'
                    while k <= 'z':
                        arr = list(word)
                        arr[j]=k
                        k=chr(ord(k)+1)

                        str1 = "".join(arr)
                        #print(str1)
                        if (str1 in set) and (str1 not in visited):
                            q.put(str1)
                            visited.append(str1)
            changes+=1
        return 0
        """

    def bfs(self, adj, start, end):
        q = deque([(start,1)])
        bfs_traversal_output=[]
        visited = set()

        while len(q) > 0:
            w,dst = q.popleft()
            visited.add(w)
            #print(w)
            for i in range(len(w)):
                key = w[:i] + "*" + w[i + 1:]

                for neig in adj[key]:
                    if neig == end:
                        #print("neig ", neig)
                        return dst +1

                    if neig not in visited:
                        #print("neig -->", neig)
                        q.append((neig, dst+1))
        return self.createAllPaths(adj,end,start)

    def createAllPaths(self, parentDict, word, beginWord):
        if word == beginWord:
            return [[beginWord]]
        output = []
        for w in parentDict[word]:
            x = self.createAllPaths(parentDict, w, beginWord)
            for l in x:
                l.append(word)
                output.append(l)
        return output

    """def bfs(self, start, end, adjList):
        visited = {}
        level={}
        parent = {}
        bfs_traversal_output = []
        queue = Queue()
        #print("adjList  --", adjList)
        for node in adjList.keys():
            visited[node]=False
            parent[node]=None
            level[node]=-1

            visited[start]=True
            level[start]=1
            queue.put(start)

            while not queue.empty():
                u = queue.get()
                print("u is ----", u)
                bfs_traversal_output.append(u)

                print("adjList[u] ----", adjList[u])
                for v in adjList[u]:
                    if not visited[v]:
                        visited[v]=True
                        parent[v]=u
                        level[v]=level[u]+1
                        queue.put[v]
            print("Output is =====", bfs_traversal_output)"""

    def ladderLength(self, start, end, wordList):
        if end not in wordList:
            return 0

        adj=self.generateAdjList(wordList)
        #print("adj ----", adj)
        return self.bfs(start, end, adj)

if __name__ == '__main__':
d = Doublet()
dictList={}
adjList = []
start=end=""

words_file = open("wordlist.txt", "r")
lines = words_file.readlines()
words_file.close()
# New dictionary with key as length of the word and value as the list of all words having that length
for key in lines:
    # Convert to lower case and remove eol character
    str = key.rstrip('\n').lower()
    lenStr = len(str)
    if lenStr in dictList.keys() :
        sameLenWords = dictList[lenStr]
        sameLenWords.append(str)
        dictList[lenStr]=sameLenWords
    else:
        sameLenWords=[]
        sameLenWords.append(str)
        dictList[lenStr]=sameLenWords
        #print("dictList[lenStr] is ", dictList[lenStr], sameLenWords)

start="milk"
end="wine"
#print("dictList is===", dictList )
print(d.ladderLength(start, end, dictList[4]))
