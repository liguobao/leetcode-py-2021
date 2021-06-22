# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树[1, 2, 2, 3, 4, 4, 3] 是对称的。


from b_tree import BinaryTree


class Solution(object):
    def array_isSymmetric(self, array):
        array_len = len(array)
        for index in range(0, int(array_len/2)):
            if array[index] != array[array_len-1-index]:
                return False
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack_node = [root]
        queue_val = []
        while(stack_node):
            stack_len = len(stack_node)
            current_val = []
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                if current_node is None:
                    current_val.append(None)
                    stack_len = stack_len - 1
                    continue
                current_val.append(current_node.val)
                if current_node.left:
                    stack_node.append(current_node.left)
                else:
                    stack_node.append(None)
                if current_node.right:
                    stack_node.append(current_node.right)
                else:
                    stack_node.append(None)
                stack_len = stack_len - 1
            print(current_val)
            if self.array_isSymmetric(current_val) is False:
                return False
        return True


tree_array_1 = [1, 2, 2, 3, 4, 4, 3]
tree_array_2 = [1, 2, 2, None, 3, None, 3]
tree_array_3 = [1, 2, 2, None, 3, 3]

# b_tree = BinaryTree(tree_array_1)
# solution_test = Solution()
# result = solution_test.isSymmetric(b_tree.root)
# print(result)


b_tree = BinaryTree(tree_array_2)
solution_test = Solution()
result = solution_test.isSymmetric(b_tree.root)
print(result)

b_tree = BinaryTree(tree_array_3)
solution_test = Solution()
result = solution_test.isSymmetric(b_tree.root)
print(result)
