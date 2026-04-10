from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LeetCode part
class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        result = ListNode()
        current = result
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            node_sum = l1val + l2val + carry
            new_node = ListNode(node_sum % 10)
            carry = node_sum // 10
            current.next = new_node
            current = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
