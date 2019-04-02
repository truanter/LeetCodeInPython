class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:
        return sorted(list(map(lambda x: x**2, A)))
