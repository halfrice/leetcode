# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Depth-first search backtracking solution
        def dfs(i: int, sum: int):
            # If the sum is zero, it matches the target and a valid combo has been found
            if sum == 0:
                # Add copy of combo to result
                res.append(combo[:])
                return
            # If i has reached the end of the candidates list or
            # the sum is less than the number at the index of candidates
            if i >= len(candidates) or sum < candidates[i]:
                return

            # Recurse without current candidate (for the next number e.g. [1,2,3..])
            dfs(i + 1, sum)
            # Add the current candidate to combo
            combo.append(candidates[i])
            # Recurse with current candidate (for including duplicates e.g. [2,2,2..])
            dfs(i, sum - candidates[i])
            # Backtrack by removing the current candidate
            combo.pop()

        combo = []
        res = []

        candidates.sort()

        dfs(0, target)

        return res
