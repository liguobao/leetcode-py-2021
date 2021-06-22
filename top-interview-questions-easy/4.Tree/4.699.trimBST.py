
from b_tree import BinaryTree


# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。
# 通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
# 修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。


class Solution(object):

    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        # 当前的值比最小值小，说明右边的需要被处理
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 当前值比最大值大，说明左边需要被处理
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # 左子树 肯定需要小于当前值
        root.left = self.trimBST(root.left, low, root.val)
        # 右子树肯定要大于当前值
        root.right = self.trimBST(root.right, root.val, high)
        return root


tree_array_1 = [1, None, 0, 0, 1]

tree_array_2 = [1, 0, 1, 0, 0, 0, 1]

tree_array_3 = [1, 1, 0, 1, 1, 0, 1, 0]


b_tree = BinaryTree(tree_array_1)
solution_test = Solution()
result = solution_test.trimBST(b_tree.root)
print(result)

b_tree = BinaryTree(tree_array_2)
solution_test = Solution()
result = solution_test.trimBST(b_tree.root)
print(result)

b_tree = BinaryTree(tree_array_3)
solution_test = Solution()
result = solution_test.trimBST(b_tree.root)
print(result)
