class Solution:
    def maxCount(self, m, n, ops):
        
    if not ops: return m*n
        return min(i[0] for i in ops)*min(j[1] for j in ops)
'''
: The method for get the matrix after calculating

l =[[0]*m for i in range(n)]
        for a,b in ops:
            for i in range(a):
                for j in range(b):
                    res[i][j]+=1
        return res
'''
