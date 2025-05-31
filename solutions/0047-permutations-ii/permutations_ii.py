# https://leetcode.com/problems/permutations-ii/


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def dfs(i: int):
            if i == len_nums:
                res.append(perm[:])
                return

            for j in range(len_nums):
                if visited[j] or (
                    j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]
                ):
                    continue

                perm[i] = nums[j]
                visited[j] = True
                dfs(i + 1)
                visited[j] = False

        nums.sort()

        len_nums = len(nums)
        visited = [False] * len_nums
        perm = [0] * len_nums
        res = []

        dfs(0)

        return res
