# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        # 'Peel' the top and right side of the matrix
        peel = matrix.pop(0)
        for i in range(len(matrix)):
            peel.append(matrix[i].pop())

        # Rotate the matrix 180 degres
        matrix.reverse()
        for i in range(len(matrix)):
            matrix[i].reverse()

        # Concat peel with a recursive call using the rotated marix
        return peel + self.spiralOrder(matrix)
