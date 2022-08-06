# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head
        slow_node = head # 一次走一步
        fast_node= head # 一次走两步
        # 快节点还有数据，都需要继续走（可能碰上环）
        while fast_node and fast_node.next:
            # 慢节点一次走一步
            s_node = slow_node.next
            # 快节点一次走两步
            f_node = fast_node.next.next
            # 当他们相遇了，说明有环，需要找到首个有环的节点
            if s_node == f_node:
                # 初始化p，去寻找首个s_node在哪
                p = head
                # p 不等于 慢节点，慢节点 +1，p +1
                while p != s_node:
                    s_node = s_node.next
                    p = p.next
                return p
            else:
                slow_node = slow_node.next
                fast_node = fast_node.next.next
        return None

head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1


result = Solution().detectCycle(head)
print(f"result:{result}")
