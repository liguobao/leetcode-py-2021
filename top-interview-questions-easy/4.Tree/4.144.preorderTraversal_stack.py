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

    # 前序遍历， 中 -> 左 -> 右
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack_node = []
        current_node = root
        while(current_node or stack_node):
            # 拿到每个节点时候，先处理自己，
            # 然后把右节点放栈，后面里面一个个再处理
            # 在把当前节点切成左边
            if current_node:
                self.queue_node.append(current_node.val)
                stack_node.append(current_node.right)
                current_node = current_node.left
            else:
                current_node = stack_node.pop()
        return self.queue_node


tree_array = [1, None, 2, 3]
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
result = Solution().preorderTraversal(b_tree.root)
print(f"result:{result}")
