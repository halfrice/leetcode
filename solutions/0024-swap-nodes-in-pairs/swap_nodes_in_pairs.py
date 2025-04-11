# https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # if not head:
        #     return None
        # elif not head.next:
        #     return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            # Swaps
            two = cur.next
            cur.next = two.next
            two.next = cur
            prev.next = two

            # Update pointers
            prev = cur
            cur = cur.next

        return dummy.next


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

        print(nums)
        return nums
