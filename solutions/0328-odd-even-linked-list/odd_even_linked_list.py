# https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        odd = head  # Odd pointer
        even = even_head = head.next  # Even pointer and save even head for later

        while even and even.next:
            # Link the odd node to the next odd node (eg. 1 -> 3)
            odd.next = even.next
            # Update the odd pointers current position (eg. pointer now at 3)
            odd = odd.next

            # Link the even node to the next even node (eg. 2 -> 4)
            even.next = odd.next
            # Update the even pointers current position (eg. pointer now at 4)
            even = even.next

        # After we have run through all possible even nodes, our odd pointer is now at
        # the last possible odd position in the linked list. We link this last node
        # to the even head we saved earlier
        odd.next = even_head

        return head


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
