# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# 给定一个二叉树 root ，返回其最大深度。

# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
class Solution(object):
    # 层次遍历的思路
    def maxDepth(self, root):
        if not root:
            return 0
        stack_node = [root]
        max_depth = 0
        while stack_node:
            # 当前这一层的所有元素
            stack_len = len(stack_node)
            # 把当前这一层全部遍历
            while stack_len > 0:
                current_node = stack_node[0]
                # current_node = stack_queue.pop()
                stack_node.remove(current_node)
                # 遍历过程把这一层的子节点放到stack_node后面(先进先出)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                # 当前node 处理完了之后就-1
                stack_len = stack_len - 1

            max_depth = max_depth + 1
        return max_depth
