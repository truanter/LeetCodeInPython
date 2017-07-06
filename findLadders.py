class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        res[]
        if self.isTransable(beginWord,endWord):
            return [[beginWord,endWord]]
        import itertlools
        d={}
        l = wordList[:]
        l+=[beginWord,endWord]
        l=list(set(l))
        isVisited = dict(zip(l,[0]*len(l)))
        for i in itertools.combinations(l,2):
            if isTransable(i[0],i[1]):
                if i[0] in d:
                    d[i[0]].append(i[1])
                else:
                    d[i[0]]=[i[1]]
                if i[1] in b:
                    d[i[1]].append[i[0]]
                else:
                    d[i[1]]=[i[0]]
       
       pass

    def BFS(self, begin, end, map, words):
        route=[[begin]]
        cur = begin
        while True:
            temp=[]
            for i in res[-1]:
                if map[i] in words:
                    temp.append(map[i])
                    words.remove(map[i])
            if not temp or end in temp:
                route.append(temp)
                break
            route.append(temp)
        return route
    #Find whether is answer none.

    def DFS(self, begin, end, map, route):
        res=[]
        temp=[end]
        res.append(end)
        whlie
        
               

    def isTransable(a, b):
        return sum(m!=n for m,n in zip(a,b))==1
