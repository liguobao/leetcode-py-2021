# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def _count(self, head):
        list_count = 0
        current_node = head
        if not current_node:
            return 0
        while current_node.next:
            list_count = list_count + 1
            current_node = current_node.next
        return list_count

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_count = self._count(head)
        remove_index = list_count - n
        if remove_index <= 0:
            return head.next
