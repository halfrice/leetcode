# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        longest = 0
        j = 0
        for i in range(len(s)):
            while s[i] in sub:
                sub.remove(s[j])
                j += 1
            sub.add(s[i])
            longest = max(longest, i - j + 1)
        return longest
