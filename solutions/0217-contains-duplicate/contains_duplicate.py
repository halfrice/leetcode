# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        history = set()
        for n in nums:
            if n in history:
                return True
            history.add(n)
        return False
