class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
        min_index = 0
        max_len = 0
        for k in range(len(s)):
            i,j = self.extend_palindrome(s, k, k )
            i1,j1 = self.extend_palindrome(s, k, k+1)
            if j-i >= j1- i1:
                cur_min_index = i
                cur_max_len = j-i+1
            else:
                cur_min_index = i1
                cur_max_len = j1-i1+1
            if cur_max_len> max_len:
                min_index, max_len = cur_min_index, cur_max_len
        #print min_index, max_len
        return s[min_index:min_index+max_len]
    def extend_palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i+1,j-1
