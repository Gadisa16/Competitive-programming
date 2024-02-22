class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max =[max(row) for row in grid]
        col_max =[max(col) for col in zip(*grid)]

        ans =0
        for r in range(len(grid)):
            for c in range(len(grid)):
                ans += min(row_max[c], col_max[r])- grid[r][c]
        return ans
        