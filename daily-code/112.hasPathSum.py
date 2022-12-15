# Definition for a binary tree node.
from b_tree import BinaryTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        stack_node = [root]
        stack_val = [root.val]
        while stack_node:
            c_node: TreeNode = stack_node[0]
            stack_node.remove(c_node)
            # 当前分支的总和
            c_val_sum = stack_val[0]
            stack_val.remove(c_val_sum)
            # 抵达叶子结点了，判断一下是否符合
            if c_node.left is None and c_node.right is None:
                if c_val_sum == targetSum:
                    return True
                continue
            if c_node.left:
                stack_node.append(c_node.left)
                stack_val.append(c_val_sum + c_node.left.val)
            if c_node.right:
                stack_node.append(c_node.right)
                stack_val.append(c_val_sum + c_node.right.val)
        return False


tree_array_1 = [1, 2]
b_tree = BinaryTree(tree_array_1)
result = Solution().hasPathSum(b_tree.root, 2)
print(result)
