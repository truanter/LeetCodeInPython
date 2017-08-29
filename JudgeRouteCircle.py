class Solution:
    def judgeCircle(self, moves):
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')
