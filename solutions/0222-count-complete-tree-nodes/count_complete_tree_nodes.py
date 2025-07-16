# https://leetcode.com/problems/count-complete-tree-nodes/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def get_depth(node):
            depth = 0

            while node:
                depth += 1
                node = node.left

            return depth

        if not root:
            return 0

        # Get the depths of subtrees
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)

        # Left subtree is for sure complete if left and right depths are equal
        if left_depth == right_depth:
            # The count of nodes formula is 2^depth - 1
            # E.g. 3 level deep full tree -> 7 nodes max exist. 2^3 is 8, minus 1 is 7, calculated 🧐
            # Bitwise left shift by left_depth (equal to 2**left_depth but faster) and recurse thru right tree
            return (1 << left_depth) + self.countNodes(root.right)
        # Right subtree is comfirmed complete if it's depth is different (less) than left
        else:
            # Recurse through left subtree and add it to calculated right number of nodes
            return self.countNodes(root.left) + (1 << right_depth)


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
