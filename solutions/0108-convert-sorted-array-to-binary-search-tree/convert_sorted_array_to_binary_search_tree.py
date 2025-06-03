# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def convert(li, ri):
            if li > ri:
                return None

            mi = (li + ri) // 2
            left = convert(li, mi - 1)
            right = convert(mi + 1, ri)

            return TreeNode(nums[mi], left, right)

        return convert(0, len(nums) - 1)


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

    def tree_to_list(self, tree: TreeNode | None, queue=deque(), depth=0) -> list:
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
                elif (
                    queue
                    and (tree.left and not tree.right)
                    or (tree.right and not tree.left)
                ):
                    queue.append(None)

        if queue:
            self.tree_to_list(queue.popleft(), queue, depth + 1)

        return self.nums
