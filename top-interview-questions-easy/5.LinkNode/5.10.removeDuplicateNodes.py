# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from link_node import arrayToLinkNode


class Solution(object):
    def distinct(self, head):
        """
        :rtype: ListNode
        """
        p_node = head
        c_node = head
        if c_node is None or c_node.next is None:
            return head
        val_set = set()
        while c_node:
            node_val = c_node.val
            if node_val not in val_set:
                # 不在字典里面，把当前node 赋值给上一个node
                # 同时当前node切换到下一个node
                p_node = c_node
                c_node = c_node.next
                val_set.add(node_val)
                continue
            # 在列表里面，上一个node的.next等于当前node的next，等于把当前node扔了
            # 然后把当前node切换到下一个node
            p_node.next = c_node.next
            c_node = c_node.next
        return head


link_1 = [1, 2, 4, 4, 6, 6]
first_node = arrayToLinkNode(link_1)
result = Solution().distinct(first_node)
print(f"link_1:{link_1},result:{result}")

link_1 = [1, 1]
first_node = arrayToLinkNode(link_1)
result = Solution().distinct(first_node)
print(f"link_1:{link_1},result:{result}")
