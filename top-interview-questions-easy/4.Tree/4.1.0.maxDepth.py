# Definition for a binary tree node.

from b_tree import BinaryTree

# 定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。


class Solution(object):
    # 直接递归走起
    def maxDepth(self, root):
        """
        :type root: T()reeNode
        :rtype: int
        """
        height = 0
        if root is None:
            return 0
        else:
            height = 1 + max(self.maxDepth(root.left),
                             self.maxDepth(root.right))
        return height


tree_array = [3, 9, 20, None, None, 15, 7]
b_tree = BinaryTree(tree_array)
solution_test = Solution()
result = solution_test.maxDepth(b_tree.root)
print(result)
