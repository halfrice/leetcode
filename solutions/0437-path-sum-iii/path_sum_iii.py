# https://leetcode.com/problems/path-sum-iii/


from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def dfs(node, sum):
            if not node:
                return 0

            # Add nodes value to the sum
            sum += node.val

            n = counts[sum - targetSum]

            # Update the count of the current path's sum
            counts[sum] += 1

            n += dfs(node.left, sum)
            n += dfs(node.right, sum)

            # Remove the count of current path's sum
            counts[sum] -= 1

            return n

        counts = Counter({0: 1})

        return dfs(root, 0)


# Utility functions
class Utils:
    def list_to_tree(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        trees = [TreeNode(n) if n is not None else None for n in nums]
        # trees = [TreeNode(n) for n in nums]

        for i, tree in enumerate(trees):
            left = 2 * i + 1
            if left < len(trees):
                tree.left = trees[left]

            right = 2 * i + 2
            if right < len(trees):
                tree.right = trees[right]

        return trees[0]
