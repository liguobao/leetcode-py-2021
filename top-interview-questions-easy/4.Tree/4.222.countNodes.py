# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from b_tree import BinaryTree


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_count = 0
        if root is None:
            return node_count
        stack_node = [root]
        while stack_node:
            stack_len = len(stack_node)
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                node_count = node_count+1
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len-1
        return node_count


tree_array_1 = [1, 2, 3, 4, 5, 6]

tree_array_2 = [1, 2, 2, 3, 3, None, None, 4, 4]


b_tree = BinaryTree(tree_array_1)
solution_test = Solution()
result = solution_test.countNodes(b_tree.root)
print(result)

b_tree = BinaryTree(tree_array_2)
solution_test = Solution()
result = solution_test.countNodes(b_tree.root)
print(result)
