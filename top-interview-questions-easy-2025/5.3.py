#给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

# 示例 1：


# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 示例 2：


# 输入：head = [1,2]
# 输出：[2,1]
# 示例 3：

# 输入：head = []
# 输出：[]
#  

# 提示：

# 链表中节点的数目范围是 [0, 5000]
# -5000 <= Node.val <= 5000
#  

# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnnhm6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        return prev
            
            

            
            