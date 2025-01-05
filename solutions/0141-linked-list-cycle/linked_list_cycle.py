# https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        history = set()
        cur = head

        while cur:
            if cur in history:
                return True
            history.add(cur)
            cur = cur.next

        return False


# Utility function for converting a list to a linked list with a cycle
class Utils:
    def list_to_linked_list(self, nums: int, pos: int) -> ListNode | None:
        dummy = ListNode(0)
        cur = dummy
        index = -1
        save = None

        for i in range(len(nums)):
            if index > -1 and index == pos:
                save = cur

            cur.next = ListNode(nums[i])
            cur = cur.next
            index += 1

            if i == len(nums) - 1:
                cur.next = save

        return dummy.next
