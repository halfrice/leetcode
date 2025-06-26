# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        # O(n^2) solution

        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = head
        cur = head.next

        while cur:
            # If the nodes don't need to swap, move prev and cur ahead 1 node
            if prev.val <= cur.val:
                prev = cur
                cur = cur.next
            # The two nodes need to be swapped
            else:
                # Insertion example (first iteration)
                # Example list: 4 -> 2 -> 1 -> 3

                # Find the position to insert at.
                # Insert will traverse the linked list until a valid position is found.
                # In this example, 4 is greater than 2, so the while loop is skipped over and
                # insert stays at its initial position.
                insert = dummy
                while insert.next.val <= cur.val:
                    insert = insert.next
                # dummy0 -> 4 -> 2 -> 1 -> 3
                #      ^ins ^prv ^cur

                temp = cur.next  # Save the 1 node
                # 0 -> 4 -> 2 -> 1 -> 3
                # ^ins ^prv ^cur ^tmp

                cur.next = insert.next  # 2's next is 4
                # 0 -> 4 <- 2 xx 1 -> 3
                # ^ins ^prv ^cur ^tmp

                insert.next = cur  # 0's next is 2
                # 0 -> 2 -> 4 xx 1 -> 3
                # ^ins ^cur ^prv ^tmp

                prev.next = temp  # 4's next is 1
                # 0 -> 2 -> 4 -> 1 -> 3
                # ^ins ^cur ^prv ^tmp

                cur = temp  # cur(2) becomes 1
                # 0 -> 2 -> 4 -> 1 -> 3
                # ^ins      ^prv ^cur/tmp

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
