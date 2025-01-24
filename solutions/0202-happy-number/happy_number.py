# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()

        while n not in history:
            history.add(n)
            n = self.squares_sum(n)

            if n == 1:
                return True

        return False

    def squares_sum(self, n: int) -> int:
        sum = 0

        while n:
            d = n % 10
            d = d**2
            sum += d
            n = n // 10

        return sum
