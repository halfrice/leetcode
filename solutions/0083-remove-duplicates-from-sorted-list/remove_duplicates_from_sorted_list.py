# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


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
