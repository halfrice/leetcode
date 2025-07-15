# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        res = []

        if not root:
            return res

        queue = deque([root])

        while queue:
            nums = []

            for i in range(len(queue)):
                cur = queue.popleft()

                nums.append(cur.val)

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            res.append(sum(nums) / len(nums))

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
