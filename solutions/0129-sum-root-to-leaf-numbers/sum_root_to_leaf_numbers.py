# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node, sum):
            if not node:
                return 0

            sum = (sum * 10) + node.val

            if not node.left and not node.right:
                return sum

            return dfs(node.left, sum) + dfs(node.right, sum)

        return dfs(root, 0)


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
