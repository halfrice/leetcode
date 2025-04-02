# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head

        # Get the length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # Determine the true amount of rotations needed
        k %= length
        if k == 0:
            return head

        # Two pointer method, fast and slow
        slow = fast = head

        # Move fast pointer k steps ahead
        for _ in range(k):
            fast = fast.next

        # Move slow and fast until fast reaches the end of the list
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Slow pointer is at the preceeding node of the new head
        new_head = slow.next
        slow.next = None  # New tail
        fast.next = head  # Old tail points to old head

        return new_head


# Utility functions for testing
class Utils:
    def list_to_linked_list(self, nums: int) -> ListNode | None:
        dummy = ListNode()
        cur = dummy

        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next

        return dummy.next

    def linked_list_to_list(self, linked_list: list[int]) -> list[int]:
        nums = []
        cur = linked_list

        while cur:
            nums.append(cur.val)
            cur = cur.next

        return nums
