# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from b_tree import BinaryTree

class Solution(object):
    
    def _dep_count(self, root):
        if not root :
            return 0
        return 1 + max(self._dep_count(root.left), self._dep_count(root.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack_node = [root]
        while stack_node:
            stack_len = len(stack_node)
            while stack_len >0:
                c_node = stack_node[0]
                stack_node.remove(c_node)
                _dep_count = self._dep_count(c_node.left) - self._dep_count(c_node.right)
                if _dep_count >1 or _dep_count < -1:
                    return False
                if c_node.left:
                    stack_node.append(c_node.left)
                if c_node.right:
                    stack_node.append(c_node.right)
                stack_len = stack_len-1
        return True


tree_array_1 = [3, 9, 20, None, None, 15, 7]
b_tree = BinaryTree(tree_array_1)
result = Solution().isBalanced(b_tree.root)
print(result)