# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        self.min_diff = float('inf')
        self.prev_val = -float('inf')

        # In-order traversal
        def iot(node):
            if not node:
                return

            iot(node.left)

            self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val

            iot(node.right)

        iot(root)

        return self.min_diff


# Utility functions
class Utils:
    def list_to_tree(self, nums: list[int]) -> TreeNode | None:
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
