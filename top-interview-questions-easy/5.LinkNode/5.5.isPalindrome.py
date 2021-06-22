# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from link_node import arrayToLinkNode, ListNode


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_array = []
        # 把节点的值全部放数组里面
        while head:
            node_array.append(head.val)
            head = head.next
        # 首尾往中间遍历，如果存在不相等，直接跳出
        left, right = 0, len(node_array)-1
        while left < right:
            if node_array[left] != node_array[right]:
                return False
            else:
                left = left + 1
                right = right - 1
        return True


test1 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(0)
node1.next = node2
node2.next = node3
test1.next = node1

result = Solution().isPalindrome(test1)
print(f"test1:{test1},result:{result}")
