from b_tree import BinaryTree


# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
# 如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。


class Solution(object):

    def _tree_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self._tree_depth(root.left), self._tree_depth(root.right))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack_node = [root]
        while stack_node:
            stack_len = len(stack_node)
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                _depth = self._tree_depth(
                    current_node.left) - self._tree_depth(current_node.right)
                if _depth > 1 or _depth < -1:
                    return False
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len-1
        return True


tree_array_1 = [3, 9, 20, None, None, 15, 7]

tree_array_2 = [1, 2, 2, 3, 3, None, None, 4, 4]

# b_tree = BinaryTree(tree_array_1)
# solution_test = Solution()
# result = solution_test.isSymmetric(b_tree.root)
# print(result)


b_tree = BinaryTree(tree_array_1)
solution_test = Solution()
result = solution_test.isBalanced(b_tree.root)
print(result)

b_tree = BinaryTree(tree_array_2)
solution_test = Solution()
result = solution_test.isBalanced(b_tree.root)
print(result)
