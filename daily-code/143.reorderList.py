# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        mid_node, right_nodes = self.take_mid_node(head)
        left_current_node = head
        while left_current_node != mid_node:
            insert_node = None
            # 把右边节点拿出来
            if len(right_nodes) > 0:
                insert_node = right_nodes.pop()
            else:
                insert_node = left_current_node.next
            insert_node.next = None
            # 把当前节点下一级先拿出来
            origin_node = left_current_node.next
            # 当前节点下一级等于右边节点
            left_current_node.next = insert_node
            insert_node.next = origin_node
            left_current_node = origin_node
        left_current_node.next =None
        return head

    def take_mid_node(self, head):
        slow_node = fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next
            if fast_node:
                fast_node = fast_node.next
        mid_node = slow_node
        right_nodes = []
        current_node = mid_node.next
        while current_node:
            right_nodes.append(current_node)
            current_node = current_node.next
        return mid_node, right_nodes


list_val = [1, 2, 3, 4]
def parse_to_link(list_val):
    head = ListNode(0)
    current_node = head
    for i in list_val:
        item_node = ListNode(i)
        current_node.next = item_node
        current_node = current_node.next
    return head.next
head = parse_to_link(list_val)
reuslt = Solution().reorderList(head)
