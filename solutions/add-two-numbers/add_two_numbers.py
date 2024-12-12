# add_two_numbers.py
# leetcode.com/problems/add-two-numbers

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        head = ListNode()
        cur = head
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            carry = sum // 10
            val = sum % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next


# Utility functions for converting lists to linked lists and back
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
