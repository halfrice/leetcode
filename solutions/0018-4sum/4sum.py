# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        if len(nums) < 4:
            return res

        nums.sort()

        nums_len = len(nums)
        for i in range(nums_len - 3):
            # Skip dupe vals to satisfy unique quadruplets requirement
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Find accompanying 3 nums
            for j in range(i + 1, nums_len - 2):
                # Find 2nd num and skip dupe vals
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Set left and right to after j and end of nums respectively
                left = j + 1
                right = nums_len - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum < target:
                        # Move the left pointer to the right if sum is too small
                        left += 1
                    elif sum > target:
                        # Move the right pointer to the left if sum is too large
                        right -= 1
                    else:
                        # Quadruplet discovered, append it to results array
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Advance both pointers
                        left += 1
                        right -= 1

                        # Skip dupe vals
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return res
