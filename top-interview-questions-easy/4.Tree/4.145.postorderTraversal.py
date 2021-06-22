# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from b_tree import BinaryTree


class Solution(object):
    def __init__(self):
        self.queue_node = []

    # 后序遍历， 左 -> 右 -> 中
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if root.left is not None:
            self.postorderTraversal(root.left)
        if root.right is not None:
            self.postorderTraversal(root.right)
        self.queue_node.append(root.val)
        return self.queue_node


tree_array = [1, None, 2, 3]
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
result = Solution().postorderTraversal(b_tree.root)
print(f"result:{result}")
