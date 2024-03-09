# https://leetcode.cn/problems/validate-binary-search-tree/

# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左
# 子树
# 只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def is_bst(self, tree_node, min_val, max_val):
        if tree_node is None:
            return True
        # 不满足区间
        if not min_val < tree_node.val < max_val:
            return False
        # left 的值，小于当前节点的值 ，大于最小值
        # right的值，大于当前值，小于最大值
        return self.is_bst(tree_node.left, min_val, tree_node.val) \
            and self.is_bst(tree_node.right, tree_node.val, max_val)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_bst(root, -2 ** 32, 2**32)
