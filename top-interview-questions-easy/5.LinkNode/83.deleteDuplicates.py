# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from link_node import arrayToLinkNode


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        prev_node = head
        current_node = head.next
        while current_node:
            if current_node.val == prev_node.val:
                prev_node.next = current_node.next
                current_node = current_node.next
                continue
            prev_node = current_node
            current_node = current_node.next
        return head


link_array = [1, 2, 2, 3, 4, 5, 5]
head_node = arrayToLinkNode(link_array)
solution = Solution()
head_node = solution.deleteDuplicates(head_node)
print(head_node)

link_array = [1, 1, 1]
head_node = arrayToLinkNode(link_array)
solution = Solution()
head_node = solution.deleteDuplicates(head_node)
print(head_node)
