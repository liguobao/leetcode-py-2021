from b_tree import BinaryTree


# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        level_array = []
        stack_node = [root]
        while stack_node:
            stack_len = len(stack_node)
            one_level_node = []
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                one_level_node.append(current_node.val)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len - 1
            level_array.append(one_level_node)
        return level_array


tree_array_1 = [1, 2, 2, 3, 4, 4, 3]

# b_tree = BinaryTree(tree_array_1)
# solution_test = Solution()
# result = solution_test.isSymmetric(b_tree.root)
# print(result)


b_tree = BinaryTree(tree_array_1)
solution_test = Solution()
result = solution_test.levelOrder(b_tree.root)
print(result)
