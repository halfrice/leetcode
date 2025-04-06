# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            # The plus one
            digits[i] += 1
            digits[i] %= 10

            # If the current digit is not 9, there's no carry so return digits
            if digits[i] != 0:
                return digits

        # We only reach this return statement if every number in digits was a 9
        return [1] + digits
