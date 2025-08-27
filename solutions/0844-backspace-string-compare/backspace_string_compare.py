# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # O(n) time and O(1) space optimized solution
        def find_valid_char_index(s, i):
            # Works backwards through a string, processing backspaces until a valid
            # character is found. Returns the valid chars index.
            skips = 0

            while i >= 0:
                if s[i] == '#':
                    skips += 1
                    i -= 1
                elif skips > 0:
                    skips -= 1
                    i -= 1
                else:
                    break

            return i

        # Start from the ends of both strings
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            # Get the indexes of valid chars to compare
            i = find_valid_char_index(s, i)
            j = find_valid_char_index(t, j)

            # If both indexes are in bounds
            if i >= 0 and j >= 0:
                # Compare chars and if they don't match, the strings are not equal
                if s[i] != t[j]:
                    return False
            # If only one index is in bounds, the strings are not equal
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        # If the algo made it to this point then the strings are equal
        return True

    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     # Bruteforce Unoptimized Solution
    #     s_stack = []
    #     for c in s:
    #         if c != '#':
    #             s_stack.append(c)
    #             continue
    #
    #         if s_stack:
    #             s_stack.pop()
    #
    #     t_stack = []
    #     for c in t:
    #         if c != '#':
    #             t_stack.append(c)
    #             continue
    #
    #         if t_stack:
    #             t_stack.pop()
    #
    #     return s_stack == t_stack
