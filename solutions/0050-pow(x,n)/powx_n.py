# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Exponentation by squaring solution using divide and conquer
        # https://en.wikipedia.org/wiki/Exponentiation_by_squaring

        def xsquare(base: float, exp: int):
            res = 1.0

            while exp:
                # Check if exp is odd using bitwise operator &
                if exp & 1:
                    res *= base

                # Square the base
                base *= base
                # Then right bitshift by 1 (divide by 2)
                exp >>= 1

            return res

        # If n is positve, simply call xsquare with x and n
        # If n is negative, turn n positive and process it as if it is positive (the
        # reciprocal), then divide 1 by the result
        # https://www.mathsisfun.com/algebra/negative-exponents.html
        return xsquare(x, n) if n >= 0 else 1 / xsquare(x, -n)
