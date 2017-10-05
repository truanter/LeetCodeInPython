class Solution(object):
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            a,b = i,i
            c,d = i,i+1
            while a>=0 and b<len(s):
                if s[a]==s[b]:
                    res += 1
                else:
                    break
                a-=1
                b+=1
            while c>=0 and d<len(s):
                if s[c]==s[d]:
                    res += 1
                else:
                    break
                c-=1
                d+=1
        return res
