# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


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
