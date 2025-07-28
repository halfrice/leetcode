# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Utility functions for testing
class Utils:
    def list_to_linked_list(self, elements):
        cur = dummy = ListNode()

        for e in elements:
            cur.next = ListNode(e)
            cur = cur.next

        return dummy.next

    def linked_list_to_list(self, head):
        res = []
        cur = head

        while cur:
            res.append(cur.val)
            cur = cur.next

        return res
