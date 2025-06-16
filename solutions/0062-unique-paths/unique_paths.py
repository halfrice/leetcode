# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Hardcode the first row since every cell will only have 1 unique path
        p = [1] * n  # Paths

        # Iterate from the second row
        for x in range(1, m):
            # Iterate from the second column
            for y in range(1, n):
                # Set the current cell as the sum of the left and top cell's values
                p[y] += p[y - 1]

        return p[-1]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     # Recursive solution
    #     if m == 1 or n == 1:
    #         return 1
    #
    #     return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
