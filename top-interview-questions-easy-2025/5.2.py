# 删除链表的倒数第N个节点

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#  
# 示例 1：


# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：

# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：

# 输入：head = [1,2], n = 1
# 输出：[1]
#  

# 提示：

# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn2925/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def _count(self, head):
        node_count = 0
        if head is None:
            return 0
        while head.next:
            node_count = node_count +1
            head = head.next
        return node_count + 1
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        node_count = self._count(head=head)
        remove_index = node_count - n
        if remove_index <=0:
            return head.next
        head_index = 0
        current_node = head
        while current_node:
            head_index = head_index +1
            if head_index == remove_index:
                pass
        
        
        