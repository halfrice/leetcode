# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head:
            return None

        # Create a copy of each node and weave it into the list
        cur = head
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy
            cur = copy.next

        # Populate the random pointers of the copied nodes with their respective copies
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Seperate the original and copied lists
        cur = head
        head2 = head.next
        while cur:
            cur2 = cur.next
            cur.next = cur2.next

            if cur2.next:
                cur2.next = cur2.next.next

            cur = cur.next

        return head2


# Utility functions for testing
class Utils:
    def list_to_linked_list(self, nodes: list) -> Node | None:
        dummy = Node(0)
        cur = dummy

        # Build linked list without random pointers first
        for n in nodes:
            cur.next = Node(n[0])
            cur = cur.next

        # Index the linked list to populate random pointers next
        indexed_list = []
        cur = dummy.next
        while cur:
            indexed_list.append(cur)
            cur = cur.next

        # Set the random pointers to the correct nodes (which now exist)
        for i, n in enumerate(nodes):
            if n[0] == indexed_list[i].val:
                if n[1] is None:
                    indexed_list[i].random = None
                else:
                    indexed_list[i].random = indexed_list[n[1]]

        return dummy.next

    def linked_list_to_list(self, linked_list: list[int]) -> list[int]:
        nodes = []
        indexed_list = []
        cur = linked_list

        # Build the index of the linked list
        while cur:
            indexed_list.append(cur)
            cur = cur.next

        # Populate nodes list with [value, index of random]
        for n in indexed_list:
            node = []
            node.append(n.val)

            # Hacky n**2 job but for small test cases it's fine
            if n.random:
                for i in range(len(indexed_list)):
                    if n.random == indexed_list[i]:
                        node.append(i)
            else:
                node.append(None)

            nodes.append(node)

        return nodes
