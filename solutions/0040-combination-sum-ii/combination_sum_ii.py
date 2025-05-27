# https://leetcode.com/problems/combination-sum-ii/


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # DFS backtracking solution similar to 39. Combination Sum
        def dfs(i: int, sum: int):
            if sum == 0:
                res.append(combo[:])
                return

            if i >= len(candidates) or sum < candidates[i]:
                return

            for j in range(i, len(candidates)):
                # Skip dupes to avoid repeating the same combos
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                combo.append(candidates[j])
                # Recurse with the next index
                dfs(j + 1, sum - candidates[j])
                # Backtrack
                combo.pop()

        combo = []
        res = []

        candidates.sort()

        dfs(0, target)

        return res
