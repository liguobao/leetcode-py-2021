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
        stack_node = []
        current_node = root
        while (current_node or stack_node):
            # 要先走左节点，所以把当前节点先进栈，然后把左节点切成当前节点
            # 当前节点空了，开始获取栈里面的最先进去的，输出，然后把当前当前节点切换到右节点
            if current_node:
                stack_node.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack_node.pop()
                self.queue_node.append(current_node.val)
                current_node = current_node.right
        return self.queue_node


tree_array = [1, None, 2, 3]
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
result = Solution().inorderTraversal(b_tree.root)
print(f"result:{result}")
