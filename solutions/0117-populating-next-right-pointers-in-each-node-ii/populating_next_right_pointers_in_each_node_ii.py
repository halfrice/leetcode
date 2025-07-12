# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: 'Node' = None,
        right: 'Node' = None,
        next: 'Node' = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def link_level(cur: 'Node'):
            if not cur:
                return

            nonlocal prev, next_level

            # Set the root node for the current level if it hasn't been set yet
            next_level = next_level or cur

            # Link the previous node to the current node
            if prev:
                prev.next = cur

            # Move the previous node pointer up to current
            prev = cur

        cur = root
        # Traverse through the tree
        while cur:
            next_level = None
            prev = None

            # Traverse current level
            while cur:
                # Link nodes on current level
                link_level(cur.left)
                link_level(cur.right)

                # Move to next node
                cur = cur.next

            # Move to next level
            cur = next_level

        return root


# Utility functions
class Utils:
    def __init__(self):
        self.levels = []

    def list_to_tree(self, nums: list[int]) -> 'Node':
        if not nums:
            return None

        trees = [Node(n) if n is not None else None for n in nums]

        for i, tree in enumerate(trees):
            left = 2 * i + 1
            if left < len(trees):
                tree.left = trees[left]

            right = 2 * i + 2
            if right < len(trees):
                tree.right = trees[right]

        return trees[0]

    # Create a levels list from the root node of a tree
    def levels_list(self, node):
        res = []

        if not node:
            return res

        cur = node
        while cur:
            next_level = None

            while cur:
                if not next_level:
                    next_level = cur.left or cur.right

                res.append(cur.val)
                cur = cur.next

            res.append('#')
            cur = next_level

        return res
