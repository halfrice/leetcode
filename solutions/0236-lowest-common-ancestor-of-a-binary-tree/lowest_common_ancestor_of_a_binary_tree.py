# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)

        if left_ancestor and right_ancestor:
            return root

        if left_ancestor:
            return left_ancestor
        return right_ancestor


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

    def get_node_with_val(self, node, val):
        if not node:
            return

        if node.val == val:
            return node

        left = self.get_node_with_val(node.left, val)
        right = self.get_node_with_val(node.right, val)

        return left or right
