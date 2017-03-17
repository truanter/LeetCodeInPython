class Solution(obj):
    def constructRectangle(self, area):
        '''
        :type area: int
        :rtype: List[int]
        '''
        import math
        s=int(math.floor(math.sqrt(area)))
        l=[i for i in range(1,s+1) if area % i==0 and i<=s][-1]
        return(int(area/l),l)
