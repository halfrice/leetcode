# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return 0

            max_left = max(0, dfs(node.left))
            max_right = max(0, dfs(node.right))

            nonlocal max_sum
            max_sum = max(max_sum, node.val + max_left + max_right)

            return node.val + max(max_left, max_right)

        max_sum = float('-inf')

        dfs(root)

        return max_sum


# Utility functions
class Utils:
    def list_to_tree(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        trees = [TreeNode(n) if n is not None else None for n in nums]

        for i, tree in enumerate(trees):
            left = 2 * i + 1
            if tree and left < len(trees):
                tree.left = trees[left]

            right = 2 * i + 2
            if tree and right < len(trees):
                tree.right = trees[right]

        return trees[0]
