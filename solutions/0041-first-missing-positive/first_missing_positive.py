# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums_len = len(nums)

        # Process nums and place numbers between 1 and the length of nums at their
        # counterpart index minus 1, e.g. 1 should be placed the first index (nums[0]),
        # 2 should be placed at the second index (nums[1]), etc.
        for i in range(nums_len):
            while 1 <= nums[i] <= nums_len and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        # Iterate through nums and find the first missing positive number
        for i in range(nums_len):
            # If the index plus one does not match the number at that index,
            # it is the missing positive number
            if i + 1 != nums[i]:
                return i + 1

        # If all previous positions contain the correct integers,
        # then the first missing positive integer is num_len + 1
        return nums_len + 1
