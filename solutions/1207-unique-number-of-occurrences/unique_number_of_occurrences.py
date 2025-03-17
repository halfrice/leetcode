# https://leetcode.com/problems/unique-number-of-occurrences/


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Count the number of occurrences (frequencies) in arr
        freq = {}
        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        # Create a set containing all the values in freq
        unique = set()
        for v in freq.values():
            if v in unique:
                return False
            unique.add(v)

        return True
