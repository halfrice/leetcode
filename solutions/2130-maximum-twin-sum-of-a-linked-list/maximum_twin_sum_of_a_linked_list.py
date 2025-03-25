# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        def reverse(node):
            prev = None
            cur = node

            while cur:
                # Save next node
                next = cur.next

                # Reverse the link so that cur.next points to prev
                cur.next = prev
                prev = cur

                # Move to the next node
                cur = next

            return prev

        # Traverse to the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Split the linked list
        left_head = head
        right_temp = slow.next
        slow.next = None  # Break the link

        # Reverse right half
        right_head = reverse(right_temp)

        # Find the max sum
        max_sum = 0
        while left_head and right_head:
            cur_sum = left_head.val + right_head.val
            max_sum = max(max_sum, cur_sum)
            left_head = left_head.next
            right_head = right_head.next

        return max_sum


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
