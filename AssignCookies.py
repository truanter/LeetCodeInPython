class Solution(object):
    def findContentChildren(self, g, s):
        '''
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        '''
        g.sort()
        s.sort()
        m=0
        while len(g) and len(s):
            if s[0] >= g[0]:
                s.remove(s[0])
                g.remove(g[0])
                m += 1
            else:
                s.remove(s[0])
        return m
