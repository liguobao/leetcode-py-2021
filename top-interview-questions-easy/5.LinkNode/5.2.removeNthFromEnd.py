# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn2925/

from link_node import arrayToLinkNode


class Solution(object):

    def _node_count(self, head):
        length = 0
        if not head:
            return 0
        while head.next:
            length = length + 1
            head = head.next
        return length + 1

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        link_count = self._node_count(head)
        remove_index = link_count - n
        if remove_index <= 0:
            return head.next
        head_index = 0
        current_node = head
        while current_node:
            head_index = head_index + 1
            if head_index == remove_index:
                if current_node.next is not None:
                   current_node.next = current_node.next.next
                else:
                    current_node.next = None
                break
            current_node = current_node.next
        return head


link_array = [1]
first_node = arrayToLinkNode(link_array)
solution = Solution()
solution._node_count(first_node)
head_node = solution.removeNthFromEnd(first_node, 1)
print(head_node)
