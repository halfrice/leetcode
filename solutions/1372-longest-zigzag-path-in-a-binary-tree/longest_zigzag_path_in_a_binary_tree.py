# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def dfs(node, left, right):
            if not node:
                return

            nonlocal longest
            longest = max(longest, left, right)

            # Recurse left from right side while increasing length by 1
            dfs(node.left, right + 1, 0)
            # Recurse right from left side while increasing length by 1
            dfs(node.right, 0, left + 1)

        longest = 0

        dfs(root, 0, 0)

        return longest


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
