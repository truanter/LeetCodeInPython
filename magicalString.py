class Solution(object):
    def magicalString(self, n):
        count=0
        l = []
        while len(l)<n:
            if len(l)<2:
                l += [count%2+1]*(count+1)
            else:
                l += [count%2+1]*l[count]
            count += 1
        return l[:n].count(1)
#version 2
class Solution(object):
    def magicalString(self, n):
        l = [1,2,2]
        i = 2
        while len(l)<n:
            l += l[i]*[3-l[-1]]
            i += 1
        return l[:n].count(1)
if __name__=='__main__':
    s = Solution()
    print(s.magicalString(6))
