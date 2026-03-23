# 回文链表
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

#  

# 示例 1：


# 输入：head = [1,2,2,1]
# 输出：true
# 示例 2：


# 输入：head = [1,2]
# 输出：false
#  

# 提示：

# 链表中节点数目在范围[1, 105] 内
# 0 <= Node.val <= 9
#  

# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnv1oc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head and head.next is None:
            return True
        values = []
        while head:
            values.append(head.val)
            head = head.next
        node_size  = len(values)
        middle_index = node_size //2
        for i in range(middle_index):
            if values[i] != values[node_size - i]:
                return False
        return True
        