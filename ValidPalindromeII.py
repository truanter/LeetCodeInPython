class Solution:
    def validPalindrome(self, s):
        if s[::-1]==s: return True
        i,j = 0, len(s)-1
        while True:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
        sub1 = s[:i]+s[i+1:]
        sub2 = s[:j]+s[j+1:]
        return sub1[::-1]==sub1 or sub2[::-1]==sub2
