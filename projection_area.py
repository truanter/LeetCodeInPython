class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        left = sum(map(lambda x: max(x), grid))
        front = sum(map(lambda x: max(x), [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]))
        buttom = 0
        for i in grid:
            for j in i:
                if j:
                    buttom += 1

        return left + front + buttom

    def projectionArea_1(self, grid):
        buttom = 0
        left = 0
        max_left = 0
        max_front = [0]*len(grid[0])
        for i in grid:
            for j in range(len(i)):
                max_left = max(i[j], max_left)
                if i[j]:
                    buttom += 1
                if i[j] > max_front[j]:
                    max_front[j] = i[j]
            left += max_left
            max_left = 0
        return left + buttom + sum(max_front)
