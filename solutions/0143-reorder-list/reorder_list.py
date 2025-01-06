# https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        # Find the midpoint of list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half of list
        right = slow.next
        slow.next = None
        prev = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        # Merge the two halves
        left = head
        right = prev
        while right:
            temp_left = left.next
            temp_right = right.next
            left.next = right
            right.next = temp_left
            left = temp_left
            right = temp_right


class Utils:
    def list_to_linked_list(self, nums: int) -> ListNode | None:
        dummy = ListNode()
        cur = dummy
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next

    def linked_list_to_list(self, linked_list: ListNode | None) -> list[int]:
        nums = []
        cur = linked_list
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return nums
