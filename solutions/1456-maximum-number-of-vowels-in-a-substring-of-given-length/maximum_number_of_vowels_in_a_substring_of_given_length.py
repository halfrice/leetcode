# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = 0

        # Count the number of vowels of the first k elements in s
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Iterate through the rest of s and update count and max_count
        for i in range(k, len(s)):
            # If the last char from the previous iteration is a vowel, subtract 1
            if s[i - k] in vowels:
                count -= 1
            # If the new char from this iteration is a vowel, add 1
            if s[i] in vowels:
                count += 1
            max_count = max(count, max_count)

        return max_count
