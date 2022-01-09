# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from link_node import arrayToLinkNode, ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        than_ten = False
        head = ListNode(0)
        p_node = head
        l1_node: ListNode = l1
        l2_node: ListNode = l2
        while l1_node or l2_node:
            now_node = ListNode(0)
            if than_ten:
                now_node.val = now_node.val + 1
                than_ten = False
            if l1_node:
                now_node.val = now_node.val + l1_node.val
                l1_node = l1_node.next
            if l2_node:
                now_node.val = now_node.val + l2_node.val
                l2_node = l2_node.next
            if now_node.val >= 10:
                now_node.val = now_node.val % 10
                than_ten = True
            p_node.next = now_node
            p_node = now_node
        if than_ten:
            now_node = ListNode(1)
            p_node.next = now_node
        return head.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]
first_node = arrayToLinkNode(l1)
tow_node = arrayToLinkNode(l2)
result = Solution().addTwoNumbers(first_node, tow_node)
print(l1)
print(l2)
print(result)
