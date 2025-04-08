# https://leetcode.com/problems/search-in-a-binary-search-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# Utility functions
class Utils:
    def __init__(self):
        self.nums = []

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

    def tree_to_list(self, tree: list[TreeNode], queue=deque()) -> list:
        if not tree:
            return []

        self.nums.append(tree.val)

        [queue.append(node) for node in [tree.left, tree.right] if node]
        if queue:
            self.tree_to_list(queue.popleft(), queue)

        return self.nums
