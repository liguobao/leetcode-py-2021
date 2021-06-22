# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from link_node import arrayToLinkNode, ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow_node = head
        fast_node = head.next
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                return True
        return False
    
    def has_cycle(self, head):
        if head is None:
            return False
        node_queue = set()
        while head:
            if head.next in node_queue:
                return True
            node_queue.add(head)
            head = head.next
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
