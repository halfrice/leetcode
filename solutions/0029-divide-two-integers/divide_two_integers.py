# https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Save the sign for later
        sign = -1 if (dividend * divisor) < 0 else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        total = 0

        while dividend >= divisor:
            # Count how many times the divisor can be doubled
            count = 0

            # Double the divisor as much as possible while remaining less than dividend
            while dividend >= (divisor << (count + 1)):
                count += 1

            # Increase total by the number of times divisor was doubled
            total += 1 << count
            # Decrease dividend by divisor doubled by count amount of times
            dividend -= divisor << count

        res = sign * total

        # If result is lower than -2**31 then set result to -2**31
        res = max(-(2**31), res)
        # if result is higher than 2**31-1 then set result to 2**31-1
        res = min(2**31 - 1, res)

        return res
