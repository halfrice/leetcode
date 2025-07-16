# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []

        if not root:
            return res

        queue = deque([root])

        while queue:
            # Current level value store
            level = []

            # Iterate through all current level nodes
            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                # Add next levels nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Current level is 'odd' (left to right)
            if not len(res) % 2 == 0:
                res.append(level)
            # Current level is 'even' (right to left)
            else:
                res.append(level[::-1])

        return res


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
