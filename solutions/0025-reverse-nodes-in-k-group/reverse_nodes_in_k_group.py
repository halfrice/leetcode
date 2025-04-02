# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def reverse_list(head):
            prev = None
            cur = head

            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            return prev

        dummy = ListNode(next=head)
        k_prev = dummy

        while head:
            # Check there are enough nodes to reverse
            count = 0
            cur = head

            while count < k and cur:
                cur = cur.next
                count += 1

            # If enough nodes to reverse were found
            if count == k:
                # Traverse to the kth node
                k_tail = head

                for _ in range(k - 1):
                    k_tail = k_tail.next

                k_next = k_tail.next  # Save the node after k to reattach
                k_tail.next = None  # Detach at the tail
                k_head = reverse_list(head)  # Reverse k nodes

                # Reconnect reversed k nodes
                k_prev.next = k_head  # Reattach (dummy or kth later node) to reversed k
                head.next = k_next

                # Move prev_group and head for next traversal
                k_prev = head
                head = k_next
            else:
                break

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

        return nums
