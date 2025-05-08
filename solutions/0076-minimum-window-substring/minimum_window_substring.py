# https://leetcode.com/problems/minimum-window-substring/


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        # Create char frequency of t's values
        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        w_freq = {}
        valid_chars = 0
        min_size = float('inf')
        min_left = -1
        left = 0

        for right, c in enumerate(s):
            # Add char to window
            w_freq[c] = w_freq.get(c, 0) + 1

            # If the window has enough of this char
            if c in t_freq and t_freq[c] >= w_freq[c]:
                valid_chars += 1

            # If window has all chars needed
            while valid_chars == len(t):
                # Update window size if it's smaller than min_size
                w = right - left + 1
                if w < min_size:
                    min_size = w
                    min_left = left

                if s[left] in t_freq and t_freq[s[left]] >= w_freq[s[left]]:
                    valid_chars -= 1

                # Shrink window from left side
                w_freq[s[left]] -= 1
                left += 1

        return '' if min_left < 0 else s[min_left : min_left + min_size]
