# https://leetcode.com/problems/find-the-highest-altitude/


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = 0
        max_alt = alt

        for n in gain:
            alt += n
            max_alt = max(alt, max_alt)

        return max_alt
