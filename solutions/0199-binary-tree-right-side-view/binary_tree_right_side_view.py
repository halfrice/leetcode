# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res = []

        if not root:
            return res

        queue = deque([root])

        while queue:
            res.append(queue[-1].val)

            for i in range(len(queue)):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

        return res

    # def rightSideView(self, root: TreeNode | None) -> list[int]:
    #     def dfs(node, depth):
    #         if not node:
    #             return
    #
    #         nonlocal res
    #
    #         if len(res) <= depth:
    #             res.append(node.val)
    #
    #         dfs(node.right, depth + 1)
    #         dfs(node.left, depth + 1)
    #
    #     if not root:
    #         return []
    #
    #     res = []
    #
    #     dfs(root, 0)
    #
    #     return res


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
