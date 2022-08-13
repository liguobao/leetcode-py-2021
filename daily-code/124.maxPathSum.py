# Definition for a binary tree node.
from re import S
from b_tree import BinaryTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self) -> None:
        self.max_path_sum = float("-inf")

    def max_gain(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # 获取左侧最大值
        max_left_sum = max(self.max_gain(root.left), 0)
        # 获取右侧最大值
        max_right_sum = max(self.max_gain(root.right), 0)
        # 当前 + 左侧 + 右侧
        current_sum = root.val + max_left_sum + max_right_sum
        # 系统中最大值 和当前最大值
        self.max_path_sum = max(self.max_path_sum, current_sum)
        # 返回要不当前 + 左侧 要不 + 右侧
        return root.val + max(max_left_sum, max_right_sum)
    
    def maxPathSum(self, root):
        self.max_gain(root)
        return self.max_path_sum


null = None
root = [-10, 9, 20, null, null, 15, 7]
tree = BinaryTree(root)
result = Solution().max_gain(tree.root)
print(result)
