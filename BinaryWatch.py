class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        l=[]
        t=[2**i for i in range(4)[::-1]]+[2**i for i in range(6)[::-1]]
        d=dict(zip(range(10),t))
        import itertools
        q=list(itertools.combinations(range(10),num))
        for i in q:
            h,m=0,0
            for j in i:
                if j<4:
                    h+=d[j]
                else:
                    m+=d[j]
            if h<12 and m<60:
                l.append(str(h)+':'+str(m).zfill(2))
        return l
