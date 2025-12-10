# leetcode.com/problems/transpose-matrix/


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # List comprehension solution
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0

        return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

    # def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
    #     # Long form solution
    #     rows = len(matrix)
    #     cols = len(matrix[0]) if rows else 0
    #     res = []
    #
    #     for j in range(cols):
    #         new_row = []
    #
    #         for i in range(rows):
    #             new_row.append(matrix[i][j])
    #
    #         res.append(new_row)
    #
    #     return res
