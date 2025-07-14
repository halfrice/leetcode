# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        cur = root

        while cur:
            # Process the left subtree
            if cur.left:
                # Set the subtree's root
                sub = cur.left

                # Get the farthest right node of the subtree
                while sub.right:
                    sub = sub.right

                # Set the subtree's right child to the cur's right child
                sub.right = cur.right
                # Swap left child to right
                cur.right = cur.left
                # Set left to None
                cur.left = None

            # Move cur up to the next right node
            cur = cur.right


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

    def tree_to_list(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        cur = root
        res = [cur.val]

        while cur.right:
            res.append(None)
            res.append(cur.right.val)

            cur = cur.right

        return res
