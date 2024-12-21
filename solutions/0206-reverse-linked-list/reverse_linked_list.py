# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur = head
        prev = None
        while cur:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
        return prev


# Utility functions for testing
class Utils:
    def list_to_linked_list(self, nums: int) -> ListNode | None:
        head = ListNode()
        cur = head
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next

    def linked_list_to_list(self, linked_list: list[int]) -> list[int]:
        nums = []
        cur = linked_list
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return nums
