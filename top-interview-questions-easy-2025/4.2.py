# 验证二叉搜索树
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 严格小于 当前节点的数。
# 节点的右子树只包含 严格大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#  

# 示例 1：


# 输入：root = [2,1,3]
# 输出：true
# 示例 2：


# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#  

# 提示：

# 树中节点数目范围在[1, 104] 内
# -231 <= Node.val <= 231 - 1

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn08xg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def is_bst(self, current_node, min_val, max_val):
        if current_node is None:
            return True
        if not min_val < current_node.val < max_val:
            return False
        return self.is_bst(current_node.left, min_val, current_node.val) and self.is_bst(current_node.right, current_node.val, max_val)
    
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        return self.is_bst(root, -2 **32, 2**32)
        
        