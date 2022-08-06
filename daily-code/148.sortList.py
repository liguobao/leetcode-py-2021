# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        return self.sort_func(head, None)

    def sort_func(self, head, tail):
        # 没有节点，直接返回
        if not head:
            return head
        # 单个节点或者尾结点
        if head.next == tail:
            head.next = None
            return head
        # 慢节点一次走一步，快节点一次走两步
        # 快节点抵达尾结点，慢节点刚好就是重点
        slow_node = fast_node = head
        while fast_node != tail:
            slow_node = slow_node.next
            fast_node = fast_node.next
            # 不是尾结点，快节点多走一步
            if fast_node != tail:
                fast_node = fast_node.next
        mid_node = slow_node

        return self.merge_list(
            self.sort_func(head, mid_node),
            self.sort_func(mid_node, tail))

    # 合并链表
    def merge_list(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        merge_result = ListNode(0)
        current_merge_node = merge_result
        current_list1 = list1
        current_list2 = list2
        while current_list1 and current_list2:
            if current_list1.val <= current_list2.val:
                current_merge_node.next = current_list1
                current_list1 = current_list1.next
            else:
                current_merge_node.next = current_list2
                current_list2 = current_list2.next
            current_merge_node = current_merge_node.next
        current_merge_node.next = current_list1 if current_list1 else current_list2
        return merge_result.next
