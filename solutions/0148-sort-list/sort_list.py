# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # O(n log n) Top-down mergesort solution

        if not head or not head.next:
            return head

        # Find the middle of the linked list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the lists and recursively call sortList on each half
        head2 = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(head2)

        # Merge left and right sorted lists
        cur = dummy = ListNode()
        while left and right:
            # Compare and attach the smaller value to cur
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next

            # Move cur ahead and keep building the merged list
            cur = cur.next

        # Add the leftover elements
        cur.next = left or right

        return dummy.next


class Utils:
    def list_to_linked_list(self, nums: int) -> ListNode | None:
        dummy = ListNode()
        cur = dummy

        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next

        return dummy.next

    def linked_list_to_list(self, head):
        res = []
        cur = head

        while cur:
            res.append(cur.val)
            cur = cur.next

        return res
