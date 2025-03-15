# https://leetcode.com/problems/max-number-of-k-sum-pairs/


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()

        ops = 0
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
                j -= 1
                ops += 1

        return ops
