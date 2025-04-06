# https://leetcode.com/problems/path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(node, sum):
            if not node:
                return False

            sum += node.val

            if not node.left and not node.right and sum == targetSum:
                return True

            return dfs(node.left, sum) or dfs(node.right, sum)

        return dfs(root, 0)


# Utility functions
class Utils:
    def list_to_tree(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        trees = [TreeNode(n) for n in nums]

        for i, tree in enumerate(trees):
            left = 2 * i + 1
            if left < len(trees):
                tree.left = trees[left]

            right = 2 * i + 2
            if right < len(trees):
                tree.right = trees[right]

        return trees[0]
