class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        import re
        from functools import reduce
        s = re.findall('[+-]?[0-9]+/[0-9]+',expression)
        r = reduce(self.add, s)
        l = r.split('/')
        u,d = l[0],l[1]
        g = self.bcd(abs(int(u)),abs(int(d)))
        u = str(int(int(u)/g))
        d = str(int(int(d)/g))
        return u+'/'+d
    def bcd(self,m,n):
        if not m :
            return n
        if not n:
            return m
        if m>=n:
            if not m%n:
                return n
            else:
                return self.bcd(n,m%n)
        else:
            return self.bcd(n,m)
    def add(self,a,b):
        r1 = a.split('/')
        r2 = b.split('/')
        d = int(r1[1])*int(r2[1])
        u = int(r1[0])*int(r2[1])+int(r2[0])*int(r1[1])
        return str(u)+'/'+str(d)
