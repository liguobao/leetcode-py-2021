class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        # 交换左右节点
        left_node = root.left
        root.left = root.right
        root.right = left_node

        # 递归交换
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root