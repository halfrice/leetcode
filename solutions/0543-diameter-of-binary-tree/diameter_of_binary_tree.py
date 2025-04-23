# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return 0

            nonlocal diameter

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        diameter = 0

        dfs(root)

        return diameter


# Utility functions
class Utils:
    def __init__(self):
        self.nums = []

    def list_to_tree(self, nums: list[int]) -> TreeNode | None:
        self.nums = []

        if not nums:
            return None

        trees = [TreeNode(n) if n is not None else None for n in nums]

        for i, tree in enumerate(trees):
            left = 2 * i + 1
            if left < len(trees):
                tree.left = trees[left]

            right = 2 * i + 2
            if right < len(trees):
                tree.right = trees[right]

        return trees[0]
