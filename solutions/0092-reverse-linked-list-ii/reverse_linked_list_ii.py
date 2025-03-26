# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        # If the length of the list is 1 or the length of the reversal is 0
        if not head.next or left == right:
            return head

        # Create a dummy node for the edge case of the reversal including head
        dummy = ListNode()
        dummy.next = head

        # Save the preceeding node before left index
        left_tail = dummy
        for _ in range(left - 1):
            left_tail = left_tail.next

        # Save the head of the sub list to be reversed
        sub_head = left_tail.next
        cur = sub_head
        prev = None

        # Reverse from left to right indexes
        for _ in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # Reconnect the severed links
        left_tail.next = prev
        sub_head.next = cur

        return dummy.next


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
