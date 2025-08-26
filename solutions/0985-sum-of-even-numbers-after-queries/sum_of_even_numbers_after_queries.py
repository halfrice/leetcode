# https://leetcode.com/problems/sum-of-even-numbers-after-queries/


class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        answer = []
        even_sum = sum(n for n in nums if n % 2 == 0)

        for v, i in queries:
            # Check if value at nums[i] is even
            if nums[i] % 2 == 0:
                # If it is, subtract from even_sum in case the value at nums[i] becomes odd
                even_sum -= nums[i]

            # Add the value from query to nums[i]
            nums[i] += v

            # Check if new value at nums[i] is even
            if nums[i] % 2 == 0:
                # If it is, add it to even_sum
                even_sum += nums[i]

            answer.append(even_sum)

        return answer
