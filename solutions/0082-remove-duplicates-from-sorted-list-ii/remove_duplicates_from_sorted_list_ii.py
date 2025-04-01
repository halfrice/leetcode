# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        prev = dummy = ListNode(next=head)
        cur = head

        while cur:
            # Skip duplicate nodes
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            # If prev.next == cur, then no duplicates were found
            if prev.next == cur:
                prev = cur
            # Duplicates were found
            else:
                prev.next = cur.next

            cur = cur.next

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

        print(nums)
        return nums
