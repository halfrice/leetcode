# https://leetcode.com/problems/determine-if-two-strings-are-close/


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Get the counts of both word1 and 2
        freq1 = {}
        for c in word1:
            freq1[c] = freq1.get(c, 0) + 1

        freq2 = {}
        for c in word2:
            freq2[c] = freq2.get(c, 0) + 1

        # Compare the counts as sets
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Compare the sorted values of the counts
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True
