class solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix:return []
        m,n = len(matrix),len(matrix[0])
        d = 1
        res = [matrix[0][0]]
        i,j = 0,0
        for c in range(m*n):
            res.append(matrix[i][j])
            i -= d
            j += d
            if i>=m:
                i = m-1
                j += 2
                d = -d
            if j>=n:
                j = n-1
                i += 2
                d = -d
            if i<0:
                i = 0
                d = -d
            if j<0:
                j = 0
                d = -d
        return res
