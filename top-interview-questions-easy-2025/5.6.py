# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast_head = slow_head = head
        while fast_head and fast_head.next:
            slow_head = slow_head.next
            fast_head = fast_head.next.next
            if fast_head == slow_head:
                return True
        return False