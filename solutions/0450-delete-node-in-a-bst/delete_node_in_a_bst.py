# https://leetcode.com/problems/delete-node-in-a-bst/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # If val is equal to the key, delete the node
        # If root only has one child on the left or right
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # If root has two children, then lift the successor into place
        successor = root.right
        while successor.left:
            successor = successor.left

        # Overwrite successor's val to the node to be deleted
        root.val = successor.val

        # Now delete the successor's node after the copy
        root.right = self.deleteNode(root.right, successor.val)

        return root


# Utility functions
class Utils:
    def __init__(self):
        self.nums = []

    def list_to_tree(self, nums: list[int]) -> TreeNode | None:
        self.nums = []

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
        if not tree and len(queue) == 0:
            return []
        elif not tree:
            self.nums.append(None)
        else:
            self.nums.append(tree.val)

            for node in [tree.left, tree.right]:
                if node:
                    queue.append(node)
                elif (tree.left and not tree.right) or (tree.right and not tree.left):
                    queue.append(None)

        if queue:
            self.tree_to_list(queue.popleft(), queue)

        return self.nums
