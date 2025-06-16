# https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Build a list with enough cells for the nth row and fill with 1s.
        # The goal is to build each row by modifying our list in place.
        row = [1] * (rowIndex + 1)

        # Iterate and build the triangle from the second row forward
        # since row 0 is always [1] and row 1 is [1, 1]
        for i in range(2, rowIndex + 1):
            # Iterate backwards through the "previous" row so that we can update the new row
            # in place. We go backwards because our previous row is left-biased or shifted left.
            # We could iterate forwards if we had our rows right shifted.
            for j in range(i - 1, 0, -1):
                # row[j - 1] is our previous left value, row[j] containes previous right value
                # When we add left to cell at right, we get the value for the new row at the
                # correct index.
                row[j] += row[j - 1]

        return row
