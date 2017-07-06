class Solution(object):
    def fourSumCount(self,A,B,C,D):
        d={}
        res = 0
        for i in A:
            for j in B:
                if i+j in d:
                    d[i+j]+=1
                else:
                    d[i+j]=1
        for m in C:
            for n in D:
                if -m-n in d:
                    res+=d[-m-n]
        return res

if __name__=='__main__':
    s = Solution()
    a=[1,2]
    b=[-2,-1]
    c=[-1,2]
    d=[0,2]
    print(s.fourSumCount(a,b,c,d))
