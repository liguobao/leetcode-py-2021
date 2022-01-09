# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from link_node import arrayToLinkNode, ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        c_node: ListNode = head
        first_node = head
        p_node: ListNode = head
        while c_node:
            c_next: ListNode = c_node.next
            if not c_next:
                break
            c_node.next = c_next.next
            c_next.next = c_node
            p_c_node = c_node
            c_node = c_node.next
            if first_node == head:
                first_node = c_next
            else:
                p_node.next = c_next
                p_node = p_c_node
        return first_node


input_val = [2,5,3,4,6,2,2]
tow_node = arrayToLinkNode(input_val)
result = Solution().swapPairs(tow_node)
print(result)
