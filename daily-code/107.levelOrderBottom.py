# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from b_tree import BinaryTree


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        stack_node = [root]
        results = []
        while stack_node:
            stack_len = len(stack_node)
            current_nodes = []
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                current_nodes.append(current_node.val)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len-1
            results.append(current_nodes)
        results.reverse()
        return results


tree_array = [3, 9, 20, None, None, 15, 7]
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
result = Solution().levelOrderBottom(b_tree.root)
print(f"result:{result}")
