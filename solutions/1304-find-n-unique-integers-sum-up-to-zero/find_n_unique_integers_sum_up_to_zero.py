# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/


class Solution:
    def sumZero(self, n: int) -> list[int]:
        # Create a list of nums from 1 to n - 1
        nums = list(range(1, n))

        # Add to the list the negative counterpart to the sum of all values in nums
        nums.append(-sum(nums))

        return nums
