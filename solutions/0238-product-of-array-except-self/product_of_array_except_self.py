# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len_nums):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len_nums - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
