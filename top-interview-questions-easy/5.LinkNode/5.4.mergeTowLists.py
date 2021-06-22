# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from link_node import arrayToLinkNode, ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        merge_node = ListNode(0)
        l1_current_node = l1
        l2_current_node = l2
        merge_current_node = merge_node
        # 遍历l1 l2节点，一个个往里面放
        while l1_current_node and l2_current_node:
            if l1_current_node.val <= l2_current_node.val:
                merge_current_node.next = l1_current_node
                l1_current_node = l1_current_node.next
            else:
                merge_current_node.next = l2_current_node
                l2_current_node = l2_current_node.next
            merge_current_node = merge_current_node.next
        # 剩下的节点，直接挂到merge_current_node里面去
        merge_current_node.next = l1_current_node if l1_current_node else l2_current_node
        return merge_node.next


link_1 = [1, 2, 4, 6]
link_2 = [3, 5]
first_node = arrayToLinkNode(link_1)
tow_node = arrayToLinkNode(link_2)
result = Solution().mergeTwoLists(first_node, tow_node)
print(result)
