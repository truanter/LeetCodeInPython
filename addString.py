class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = list(num1)
        b = list(num2)
        sum1=0
        n = int(a[-1]) + int(b[-1])
        i=1
        sum=n%10
        m=n/10
        a.pop()
        b.pop()
        while a and b:
            d = int(a[-1]) + int(b[-1])
            sum += (d%10+m)*10**i
            m=d/10
            i+=1
            a.pop()
            b.pop()
        if a:
            for j in a:
                sum1 = 10 * sum1 + int(j)
        if b:
            for j in b:
                sum1 = 10*sum1 + int(j)
        return str((sum1+m) * 10**i + sum)
