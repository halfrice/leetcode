# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        # This is why python is so powerful
        return ' '.join(reversed(s.split()))
