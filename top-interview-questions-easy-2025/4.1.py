# 二叉树的最大深度
# 给定一个二叉树 root ，返回其最大深度。

# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        max_depth = 0
        stack_nodes = [root]
        while stack_nodes:
            curent_count = len(stack_nodes)
            while curent_count >0:
                curent_node = stack_nodes[0]
                stack_nodes.remove(curent_node)
                if curent_node.left:
                    stack_nodes.append(curent_node.left)
                if curent_node.right:
                    stack_nodes.append(curent_node.right)
                curent_count = curent_count -1
            max_depth = max_depth +1
        return max_depth
        
        
        
        
        