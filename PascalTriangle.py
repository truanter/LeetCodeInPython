def generate(self, numRows):
        l =  [[] for i in range(numRows)]
        if numRows:
            l[0]=[1]
            if numRows >= 2:
                l[1]=[1,1]
                for i in range(2,numRows):
                    l[i].append(1)
                    for j in range(len(l[i-1])-1):
                        l[i].append(l[i-1][j]+l[i-1][j+1])
                    l[i].append(1)
        return l
