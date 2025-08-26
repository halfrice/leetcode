# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_freq = Counter(text)
        balloon_freq = Counter('balloon')
        total = float('inf')

        for k, v in balloon_freq.items():
            total = min(total, text_freq[k] // v)

        return total
