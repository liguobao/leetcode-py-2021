# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow_node = head
        fast_node = head.next
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


result = Solution().hasCycle(test1)
print(f"result:{result}")
