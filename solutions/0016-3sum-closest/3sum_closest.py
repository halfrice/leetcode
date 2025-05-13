# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        nums_len = len(nums)
        closest = float('inf')

        for i in range(nums_len - 2):
            left = i + 1
            right = nums_len - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                # Return sum if target is hit
                if sum == target:
                    return sum

                # Update closest with sum
                if abs(sum - target) < abs(closest - target):
                    closest = sum

                # Move pointers to get closer to target
                if sum < target:
                    left += 1
                else:
                    right -= 1

        return closest
