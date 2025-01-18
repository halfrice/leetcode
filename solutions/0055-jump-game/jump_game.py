# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Move the goal posts (greedy)

        goal = len(nums) - 1

        # Iterate backwards through array
        for i in range(len(nums) - 1, -1, -1):
            # If index + the value at that index can reach the goal, move the goal
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
