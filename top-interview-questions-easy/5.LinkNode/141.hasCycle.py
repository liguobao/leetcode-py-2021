# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing_extensions import TypeGuard
from link_node import arrayToLinkNode, ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        # 快慢两个节点
        # 慢节点一次走一步
        # 快节点一次走两步
        # 如果快慢都走到一起，说明有环了
        slow_node: ListNode = head
        fast_node: ListNode = head.next
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                return True
        return False


test1 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
test1.next = node1
node1.next = node2
node2.next = node3
node3.next = test1


result = Solution().has_cycle(test1)
print(f"result:{result}")
