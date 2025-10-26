# https://leetcode.com/problems/positions-of-large-groups


class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        if len(s) < 3:
            return []

        intervals = []

        # Iterate through s
        i = 0
        while i < len(s):
            # If the next element is a match, check the element after until a non-match is found
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1

            # If the length of consecutive chars is at least 3, append range to intervals
            if j - i >= 3:
                intervals.append([i, j - 1])

            # move to the next new element in s at index j
            i = j

        return intervals
