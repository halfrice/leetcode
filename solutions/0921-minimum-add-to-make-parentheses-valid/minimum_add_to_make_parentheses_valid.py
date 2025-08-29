# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        maidenless_opens = 0  # Count open parentheses
        additions = 0  # Count number of additions needed

        for c in s:
            # Add to open parens (maidenless) count
            if c == '(':
                maidenless_opens += 1
            # Subtract from open count if at least one exists and this char is closing
            elif maidenless_opens and c == ')':
                maidenless_opens -= 1
            # Add to additions needed if this is a closing with no current matching opens
            else:
                additions += 1

        # Add leftover unmatched open parentheses
        additions += maidenless_opens

        return additions
