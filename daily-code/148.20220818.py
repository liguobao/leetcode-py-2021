# Definition for singly-linked list.
from select import select


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sort_func(head, None)

    def sort_func(self, head: ListNode, tail: ListNode):
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        fast_node = head
        slow_node = head
        if fast_node != tail:
            fast_node = fast_node.next
            slow_node = slow_node.next
            if fast_node !=tail:
                fast_node = fast_node.next
        # 中间节点
        mid_node = slow_node
        return self.merge_list(self.sort_func(head, mid_node), self.sort_func(mid_node, tail))

    # 合并两个链表
    def merge_list(self, first_list: ListNode, second_list: ListNode):
        if not first_list:
            return second_list
        if not second_list:
            return first_list
        merge_list = ListNode()
        current_fisrt = first_list
        current_second = second_list
        current_merge = merge_list
        while current_fisrt and current_second:
            if current_fisrt.val <= current_second.val:
                current_merge.next = current_fisrt
                current_fisrt = current_fisrt.next
            else:
                current_merge.next = current_second
                current_second = current_second.next
            current_merge = current_merge.next
        current_merge.next = current_fisrt if current_fisrt else current_second
        return merge_list.next


fisrt_list = ListNode(1)
fisrt_list.next = ListNode(6)
second_list = ListNode(2)
second_list.next = ListNode(5)

result = Solution().merge_list(fisrt_list, second_list)
print(result)
