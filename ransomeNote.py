class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r,m=set(ransomNote),set(magazine)
        isCons = True
        for i in r:
            isCons = isCons & (ransomNote.count(i)<=magazine.count(i))
        return isCons
