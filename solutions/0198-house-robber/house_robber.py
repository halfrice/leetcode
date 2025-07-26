# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: list[int]) -> int:
        two_houses_ago = 0
        prev_house = 0

        for n in nums:
            temp = max(two_houses_ago + n, prev_house)
            two_houses_ago = prev_house
            prev_house = temp

        return prev_house
