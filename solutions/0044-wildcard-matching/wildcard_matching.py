# https://leetcode.com/problems/wildcard-matching/

from pprint import pprint


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)

        # Build a p+1 * s+1 matrix and fill with false values
        # The extra cell is to represent an empty pattern and string
        m = [[False] * (len_p + 1) for _ in range(len_s + 1)]

        # Build first row of the matrix
        m[0][0] = True  # m[0][0] represents s='', p=''
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                m[0][i] = m[0][i - 1]

        # Process matrix
        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                # If s char matches the p char or p is ?, copy the last char match to
                # keep the Truthy train going
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    m[i][j] = m[i - 1][j - 1]
                # Check if p is a star
                elif p[j - 1] == '*':
                    # If * is matched to nothing, copy the value in the cell to the left
                    # If * matches 1 or more chars, copy the value in the cell above
                    m[i][j] = m[i - 1][j] or m[i][j - 1]

        return m[-1][-1]
