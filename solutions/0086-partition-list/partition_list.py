# https://leetcode.com/problems/partition-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_cur = less_dummy = ListNode()
        more_cur = more_dummy = ListNode()
        cur = head

        while cur:
            if cur.val < x:
                less_cur.next = cur
                less_cur = less_cur.next
            else:
                more_cur.next = cur
                more_cur = more_cur.next

            cur = cur.next

        less_cur.next = more_dummy.next
        more_cur.next = None

        return less_dummy.next


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
