from b_tree import BinaryTree


# 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

# 返回移除了所有不包含 1 的子树的原二叉树。

# (节点 X 的子树为 X 本身，以及所有 X 的后代。)

class Solution(object):

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root


tree_array_1 = [1, None, 0, 0, 1]

tree_array_2 = [1, 0, 1, 0, 0, 0, 1]

tree_array_3 = [1, 1, 0, 1, 1, 0, 1, 0]

# b_tree = BinaryTree(tree_array_1)
# solution_test = Solution()
# result = solution_test.isSymmetric(b_tree.root)
# print(result)


b_tree = BinaryTree(tree_array_1)
solution_test = Solution()
result = solution_test.pruneTree(b_tree.root)
print(result)

b_tree = BinaryTree(tree_array_2)
solution_test = Solution()
result = solution_test.pruneTree(b_tree.root)
print(result)

b_tree = BinaryTree(tree_array_3)
solution_test = Solution()
result = solution_test.pruneTree(b_tree.root)
print(result)
