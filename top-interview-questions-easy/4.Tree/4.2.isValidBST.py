# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。


# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn08xg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from b_tree import BinaryTree


class Solution(object):
    def _bst(self, tree_node, min_val, max_val):
        if tree_node is None:
            return True
        # 如果不在当前节点不在允许的区间，直接扔掉
        if not min_val < tree_node.val < max_val:
            return False
        # 左节点 大于最小值，小于当前值
        # 右节点，大于当前值，小于最大值
        return self._bst(tree_node.left, min_val, tree_node.val) \
            and self._bst(tree_node.right, tree_node.val, max_val)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self._bst(root, - 2 ** 32, 2**32)


tree_array_1 = [5, 4, 6, None, None, 3, 7]
tree_array_2 = [2, 1, 3]

b_tree = BinaryTree(tree_array_1)
solution_test = Solution()
result = solution_test.isValidBST(b_tree.root)
print(result)


b_tree = BinaryTree(tree_array_2)
solution_test = Solution()
result = solution_test.isValidBST(b_tree.root)
print(result)
