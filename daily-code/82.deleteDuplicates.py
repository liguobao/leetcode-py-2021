class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def deleteDuplicatesV2(self, head: ListNode):
        if not head:
            return head
        dummy_node = ListNode(0, head)
        cur_node = dummy_node
        # 当前节点和下一级节点都存在
        # 当前节点 +下一级 或者为None，说明是单节点或者是最后一个节点，这种情况下可以终止了
        while cur_node.next and cur_node.next.next:
            # 发现了重复元素
            if cur_node.next.val == cur_node.next.next.val:
                cur_val = cur_node.val
                # 不断当前节点的Next赋值给下一个（等同于移除）
                while cur_node.next and cur_node.next.val == cur_val:
                    cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dummy_node.next

    def deleteDuplicates(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        current_node: ListNode = head
        node_val = set()
        dup_val = set()
        while current_node:
            if current_node.val in node_val:
                dup_val.add(current_node.val)
            else:
                node_val.add(current_node.val)
            current_node = current_node.next
        pre_node = head
        current_node = head
        while current_node:
            if current_node.val in dup_val:
                if current_node == head:
                    head = current_node.next
                    pre_node = current_node.next
                else:
                    pre_node.next = current_node.next
                current_node = current_node.next
                continue
            pre_node = current_node
            current_node = current_node.next
        return head


# root_head = ListNode(1)
# node_2 = ListNode(2)
# node_3_1 = ListNode(3)
# node_3_2 = ListNode(3)
# node_4_1 = ListNode(4)
# node_4_2 = ListNode(4)
# node_5 = ListNode(5)
# root_head.next = node_2
# node_2.next = node_3_1
# node_3_1.next = node_3_2
# node_3_2.next = node_4_1
# node_4_1.next = node_4_2
# node_4_2.next = node_5
# result = Solution().deleteDuplicates(root_head)
# print(result)

# root_head = ListNode(1)
# node_2 = ListNode(1)
# node_3_1 = ListNode(1)
# node_3_2 = ListNode(2)
# node_4_1 = ListNode(3)
# node_4_2 = ListNode(4)
# node_5 = ListNode(5)
# root_head.next = node_2
# node_2.next = node_3_1
# node_3_1.next = node_3_2
# node_3_2.next = node_4_1
# node_4_1.next = node_4_2
# node_4_2.next = node_5
# result = Solution().deleteDuplicates(root_head)
# print(result)


root_head = ListNode(1)
node_2 = ListNode(1)
node_3_1 = ListNode(1)
node_3_2 = ListNode(2)
node_4_1 = ListNode(3)
node_4_2 = ListNode(4)
node_5 = ListNode(5)
root_head.next = node_2
result = Solution().deleteDuplicates(root_head)
print(result)
