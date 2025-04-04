# https://leetcode.com/problems/invert-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Utility functions for testing
class Utils:
    def list_to_tree(self, nums: list[int]) -> TreeNode | None:
        self.nums = []

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

    def tree_to_list(self, tree: list[TreeNode], queue=deque()) -> None:
        if not tree:
            return None

        self.nums.append(tree.val)

        [queue.append(node) for node in [tree.left, tree.right] if node]
        if queue:
            self.tree_to_list(queue.popleft(), queue)
