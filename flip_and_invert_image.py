class Solution:
    def flipAndInvertImage(self, A: list[list[int]]) -> list[list[int]]:
        return [list(map(lambda x: 1-x, reversed(i))) for i in A]
