# https://leetcode.com/problems/increasing-triplet-subsequence/


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        sm = float('inf')
        md = float('inf')

        for n in nums:
            if n > md:
                return True

            if n <= sm:
                sm = n
            else:
                md = n

        return False
