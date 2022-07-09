from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        assert grid and grid[0]  # not a complete check that this is a matrix
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i == j or i == len(grid)-j-1:
                    if not val:
                        return False
                else:
                    if val:
                        return False
        return True


s = Solution()

assert s.checkXMatrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
assert not s.checkXMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
assert s.checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]])
assert not s.checkXMatrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]])
