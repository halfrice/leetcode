# https://leetcode.com/problems/n-queens-ii/


class Solution:
    def totalNQueens(self, n: int) -> int:
        # This problem is similar to 51. N-Queens, but easier.
        # Instead of having to create, update, and return entire valid boards, we can
        # keep a count of those same valid boards and return the total count.

        def dfs(x):
            # When x (row) equals n, all Queens are valid so increment result by 1
            if x == n:
                nonlocal res
                res += 1
                return

            # Iterate through each column (y) of the row (x)
            for y in range(n):
                # Check if placing a Queen can be done without being spawn killed
                if not cols[y] and not diag[x + y] and not neg_diag[n - x + y]:
                    # Add the Queens position to cols and diags
                    cols[y] = diag[x + y] = neg_diag[n - x + y] = True

                    dfs(x + 1)

                    # Remove the Queens position from cols and diags
                    cols[y] = diag[x + y] = neg_diag[n - x + y] = False

        cols = [False] * n
        diag = [False] * (n * 2)
        neg_diag = [False] * (n * 2)
        res = 0

        dfs(0)

        return res
