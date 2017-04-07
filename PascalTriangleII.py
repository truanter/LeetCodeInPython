class Solution(object):
    def getRow(self, rowIndex):
        l=[1]
        if rowIndex >=1:
            l*=(rowIndex+1)
            for i in range(1,rowIndex):
                for j in range(0,i):
                    l[i-j]+=l[i-j-1]
        return l
