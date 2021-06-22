# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn2925/

from link_node import arrayToLinkNode


class Solution(object):

    def reverseList(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_queue = []
        current_node = head
        while current_node:
            if not current_node:
                break
            if current_node:
                node_queue.append(current_node)
            current_node = current_node.next
        node_count = len(node_queue)
        head = None
        current_node = head
        for node_index in range(node_count-1, -1, -1):
            node_item = node_queue[node_index]
            if node_index == 0:
                node_item.next = None
            if not head:
                head = node_item
                current_node = node_item
                continue
            current_node.next = node_item
            current_node = current_node.next
        return head


link_array = [1, 2, 3, 4]
first_node = arrayToLinkNode(link_array)
solution = Solution()
head_node = solution.reverseList(first_node, 1)
print(head_node)
