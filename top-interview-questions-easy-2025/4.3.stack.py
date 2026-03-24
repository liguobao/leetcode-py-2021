# 对称二叉树
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

#  

# 示例 1：


# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：


# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  

# 提示：

# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
#  

# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn7ihv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        queue_nodes = [root.left, root.right]
        while queue_nodes:
            left = queue_nodes.pop()
            right = queue_nodes.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            # 成对入队 左边的左节点 和右边的右节点
            queue_nodes.append(left.left)
            queue_nodes.append(right.right)
            
            # 左边的右节点 和 右边的左节点
            queue_nodes.append(left.right)
            queue_nodes.append(right.left)
        return True
            
        