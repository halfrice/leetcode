# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(i: int):
            if i == len_nums:
                res.append(perm[:])
                return

            for j in range(len_nums):
                if not visited[j]:
                    visited[j] = True
                    perm[i] = nums[j]
                    dfs(i + 1)
                    visited[j] = False

        len_nums = len(nums)
        visited = [False] * len_nums
        perm = [0] * len_nums
        res = []

        dfs(0)

        return res
