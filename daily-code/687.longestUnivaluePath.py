# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from b_tree import BinaryTree


class Solution(object):
    def __init__(self):
        self.max_edge_count = 0

    def max_path_edge(self, root):
        if not root:
            return 0
        left_edge = self.max_path_edge(root.left)
        right_edge = self.max_path_edge(root.right)
        left1 = left_edge + 1 if root.left and root.left.val == root.val else 0
        right1 = right_edge + 1 if root.right and root.right.val == root.val else 0 
        self.max_edge_count = max(self.max_edge_count, left1 + right1)
        return max(left1, right1)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_edge(root)
        return self.max_edge_count


input_data = [5, 4, 5, 1, 1, 5]
tree_node = BinaryTree(input_data)
result = Solution().longestUnivaluePath(tree_node.root)
print(result)
