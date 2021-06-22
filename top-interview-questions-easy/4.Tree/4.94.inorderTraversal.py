from b_tree import BinaryTree


class Solution(object):
    def __init__(self):
        self.queue_node = []
    # 中序遍历， 左 -> 中 -> 右

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if root.left is not None:
            self.inorderTraversal(root.left)
        self.queue_node.append(root.val)
        if root.right is not None:
            self.inorderTraversal(root.right)
        return self.queue_node


tree_array = [1, None, 2, 3]
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
result = Solution().inorderTraversal(b_tree.root)
print(f"result:{result}")
