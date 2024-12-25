# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
