# https://leetcode.com/problems/harshad-number/


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        x_copy = x

        while x > 0:
            sum += x % 10
            x //= 10

        return sum if x_copy % sum == 0 else -1
