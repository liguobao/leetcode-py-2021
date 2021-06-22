from b_tree import BinaryTree


class Solution(object):
    def __init__(self):
        self.max_path_sum = float("-inf")

    def max_gain(self, tree_node):
        if tree_node is None:
            return 0
        # 计算左边的最大和
        left_gain = max(self.max_gain(tree_node.left), 0)
        # 计算右边的最大和
        right_gain = max(self.max_gain(tree_node.right), 0)

        # 计算这个路径的最大和
        price_new_path = tree_node.val + left_gain + right_gain
        # 看下这个最大和现在已有的最大和谁更大，谁大谁做主
        self.max_path_sum = max(self.max_path_sum, price_new_path)
        # 返回
        return tree_node.val + max(left_gain, right_gain)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_gain(root)
        return self.max_path_sum


tree_array = [1, 2, 3]
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
result = Solution().maxPathSum(b_tree.root)
print(f"result:{result}")
