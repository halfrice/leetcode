# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int):
            if not node:
                return node

            nonlocal count

            if max_val <= node.val:
                count += 1
                max_val = node.val

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        count = 0

        dfs(root, float('-inf'))

        return count


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
