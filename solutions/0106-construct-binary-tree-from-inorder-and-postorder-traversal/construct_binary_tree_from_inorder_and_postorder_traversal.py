# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        val_to_index = {v: i for i, v in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            root = TreeNode(postorder.pop())
            mid = val_to_index[root.val]

            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)


# Utility functions
class Utils:
    def __init__(self):
        self.nums = []
        self.max_depth = 0

    def get_max_depth(self, node, depth=0):
        if not node:
            return 0

        max_depth = depth

        if node.left or node.right:
            max_depth = max(
                self.get_max_depth(node.left, depth + 1),
                self.get_max_depth(node.right, depth + 1),
            )

        return max_depth

    def tree_to_list(self, tree: list[TreeNode], queue=deque(), depth=0) -> list:
        if depth == 0 and len(queue) == 0:
            self.nums = []
            self.max_depth = max(self.get_max_depth(tree), self.max_depth)

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
                elif (
                    not tree.left
                    and not tree.right
                    and depth <= self.max_depth
                    and depth != 0
                ):
                    queue.append(None)

        if queue:
            self.tree_to_list(queue.popleft(), queue, depth + 1)

        return self.nums
