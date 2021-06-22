from b_tree import BinaryTree

import collections

# 定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。


class Solution(object):
    # 层次遍历的思路
    def maxDepth(self, root):
        """
        :type root: T()reeNode
        :rtype: int
        """
        height = 0
        if root is None:
            return 0
        stack_node = []
        # 每一层都存储在这个栈中
        stack_node.append(root)
        max_depth = 0
        while(stack_node):
            stack_len = len(stack_node)
            # 遍历整个栈，把当前层的所有叶子节点都放在栈最后面
            while stack_len > 0:
                # 先进先出
                current_node = stack_node[0]
                stack_node.remove(current_node)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len - 1
            max_depth = max_depth + 1
        return max_depth


tree_array = [1, 2, 3, 4, None, None, 5]

b_tree = BinaryTree(tree_array)
solution_test = Solution()
result = solution_test.maxDepth(b_tree.root)
print(result)
