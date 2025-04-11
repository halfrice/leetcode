# https://leetcode.com/problems/merge-k-sorted-lists/

from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Less than magic function for PriorityQueue to compare vals
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Priority queue solution
        pq = PriorityQueue()

        # Add the first node of each list within lists
        for head in lists:
            if head:
                pq.put(head)

        dummy = ListNode()
        cur = dummy

        while not pq.empty():
            # Get the node with lowest value from pq
            node = pq.get()

            # Replace the node pulled with the nodes next if it exists
            if node.next:
                pq.put(node.next)

            # Link the node pulled by PriorityQueue and update cur pointer
            cur.next = node
            cur = cur.next

        return dummy.next

    # def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
    #     # Keep merging two lists until there is one solution
    #
    #     def mergeTwoLists(
    #         self, list1: ListNode | None, list2: ListNode | None
    #     ) -> ListNode | None:
    #         dummy = ListNode()
    #         cur = dummy
    #
    #         while list1 and list2:
    #             if list1.val < list2.val:
    #                 cur.next = list1
    #                 list1 = list1.next
    #             else:
    #                 cur.next = list2
    #                 list2 = list2.next
    #             cur = cur.next
    #
    #         if list1:
    #             cur.next = list1
    #         elif list2:
    #             cur.next = list2
    #
    #         return dummy.next
    #
    #     if not lists or len(lists) == 0:
    #         return None
    #
    #     while len(lists) > 1:
    #         merged_lists = []
    #
    #         for i in range(0, len(lists), 2):
    #             list1 = lists[i]
    #             list2 = lists[i + 1] if (i + 1) < len(lists) else None
    #             merged_lists.append(mergeTwoLists(list1, list2))
    #
    #         lists = merged_lists
    #
    #     return lists[0]


# Utility functions
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

        return nums
