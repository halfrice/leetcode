# longest_palindromic_substring.py


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            palindrome = ''
            offset = 0
            while (i + 1 + offset) < len(s) and s[i] == s[i + 1 + offset]:
                offset += 1
            j = 0
            while i - j >= 0 and i + offset + j < len(s):
                if s[i - j] == s[i + offset + j]:
                    palindrome = s[i - j : i + offset + j + 1]
                else:
                    break
                j += 1
            if len(longest) < len(palindrome):
                longest = palindrome
        return longest
