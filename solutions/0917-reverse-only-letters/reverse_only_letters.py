# https://leetcode.com/problems/reverse-only-letters/


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Two pointer solution

        # Convert s into a list so we can swap letters in place
        s = list(s)
        i = 0  # i represents the left pointer
        j = len(s) - 1  # j the right

        while i < j:
            # Find a valid alpha char on the left side the string.
            # This loop will skip all non-alphabet chars until one is found.
            while i < j and not s[i].isalpha():
                i += 1
            # Find a valid alpha char on the right
            while i < j and not s[j].isalpha():
                j -= 1

            # There is an edge case where after both while loops, i and j could pass eachother,
            # causing a swap when it should not happen. So, like the while loops above, test if
            # i is still less than j
            if i < j:
                # Swap the chars
                s[i], s[j] = s[j], s[i]
                # Move to the next chars
                i += 1
                j -= 1

        return ''.join(s)
