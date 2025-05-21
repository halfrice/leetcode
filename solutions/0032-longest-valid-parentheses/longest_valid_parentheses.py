# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Dynamic programming solution

        # Create an array with zeroes plus an extra slot to store results that are
        # shifted right by 1
        arr = [0] * (len(s) + 1)

        for i, c in enumerate(s, 1):
            # Look for closing parentheses as possible ends to valid substrings
            if c == ')':
                # Check if previous char is '(' which signals a pair
                if i > 1 and s[i - 2] == '(':
                    # Add 2 to the result two positions ago in arr
                    arr[i] = arr[i - 2] + 2
                # If prev char is ')'
                else:
                    # Get the index of the potential matching '('
                    match_i = i - arr[i - 1] - 1

                    # Check if the potential matching '(' is true
                    if match_i > 0 and s[match_i - 1] == '(':
                        # Add the value found match[i]
                        # Plus the value found previous to the current pair
                        # Then plus 2 for that current pair
                        arr[i] = arr[match_i - 1] + arr[i - 1] + 2
                        # arr[i] = arr[i - 1] + 2 + arr[match_i - 1]

        return max(arr)

    # def longestValidParentheses(self, s: str) -> int:
    #     # Stack solution
    #     stack = [-1]
    #     max_len = 0
    #
    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             stack.append(i)
    #         else:
    #             stack.pop()
    #
    #             if not stack:
    #                 stack.append(i)
    #             else:
    #                 max_len = max(max_len, i - stack[-1])
    #
    #     return max_len
