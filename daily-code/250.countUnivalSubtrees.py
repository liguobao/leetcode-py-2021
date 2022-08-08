# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ast import Not
from b_tree import BinaryTree


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        self.tree_count = 0
        self.is_uni_tree(root)
        return self.tree_count
    
    def is_uni_tree(self, node):
        # 没有左右节点，自然就是一个 同值子树
        if not node.left and not node.right:
            self.tree_count = self.tree_count +1
            return True
        is_uni = True
        if node.left is not None:
            is_uni  = is_uni and self.is_uni_tree(node.left) and node.left.val == node.val
        if node.right is not None:
            is_uni = is_uni and self.is_uni_tree(node.right) and node.right.val == node.val
        self.tree_count += is_uni
        return is_uni
        

root = [5, 1, 5, 5, 5, None, 5]
tree_root = BinaryTree(root)
result = Solution().countUnivalSubtrees(tree_root.root)
print(result)
