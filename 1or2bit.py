class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        return not len(bits[:-1:])%2 if 0 not in bits[:-1:] else not bits[-2::-1].index(0)%2
        
