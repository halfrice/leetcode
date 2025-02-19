# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head.next:
            return

        # Find the midpoint minus 1 of list
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Remove middle node
        slow.next = slow.next.next

        return head


# Utility functions for converting lists to linked lists and back
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
