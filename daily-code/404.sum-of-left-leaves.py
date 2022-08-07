# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from b_tree import BinaryTree


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.left_sum = 0
        def dfs(root):
            if root.left:
                self.left_sum = self.left_sum + root.left.val
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return self.left_sum
            

root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
tree_root = BinaryTree(root)
result = Solution().sumOfLeftLeaves(tree_root.root)
print(result)