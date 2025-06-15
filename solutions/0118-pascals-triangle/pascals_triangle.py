# https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Hardcode the first row(s) since no calculations need to be made
        triangle = [[1]] if numRows == 1 else [[1], [1, 1]]

        # Iterate and build the triangle from the second row forward
        for i in range(2, numRows):
            # Build current row
            # First element is 1
            row = [1]

            # Calculate middle elements
            for j in range(1, i):
                # Left is triangle[i-1][j-1], right is triangle[i-1[j]]
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            # Last element is 1
            row.append(1)

            # Add current row
            triangle.append(row)

        return triangle
