# https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix[0])
        cols = len(matrix)

        left = 0
        right = cols - 1
        while left <= right:
            col = (left + right) // 2
            if target < matrix[col][0]:
                right = col - 1
            elif target > matrix[col][-1]:
                left = col + 1
            else:
                break

        if not (left <= right):
            return False

        col = (left + right) // 2
        left = 0
        right = rows - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[col][mid]:
                right = mid - 1
            elif target > matrix[col][mid]:
                left = mid + 1
            else:
                return True
        return False
