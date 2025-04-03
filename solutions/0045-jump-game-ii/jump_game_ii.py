# https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        last_jump = 0
        max_dist = 0

        for i, n in enumerate(nums[:-1]):
            max_dist = max(max_dist, i + n)

            # Check if we've jumped as far as possible (max_dist) from the last jump
            if last_jump == i:
                # Set the new maximum reachable index
                last_jump = max_dist
                jumps += 1

        return jumps
