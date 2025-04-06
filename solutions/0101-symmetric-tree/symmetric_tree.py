# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(left_node: TreeNode, right_node: TreeNode):
            if not left_node and not right_node:
                return True

            if not left_node or not right_node or left_node.val != right_node.val:
                return False

            return is_mirror(left_node.left, right_node.right) and is_mirror(
                left_node.right, right_node.left
            )

        return is_mirror(root, root)


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
