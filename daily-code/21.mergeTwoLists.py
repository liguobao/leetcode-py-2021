# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        merge_node = ListNode(0)
        list1_node: ListNode = list1
        list2_node: ListNode = list2
        merge_current_node = merge_node
        while list1_node and list2_node:
            if list1_node.val <= list2_node.val:
                merge_current_node.next = list1_node
                list1_node = list1_node.next
            else:
                merge_current_node.next = list2_node
                list2_node = list2_node.next
            merge_current_node = merge_current_node.next
        # 最后的数据添加到合并后的节点
        merge_current_node.next = list1_node if list1_node else list2_node
        return merge_node.next
