class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total_num = 0
        # 节点
        stack_node = [root]
        # 每一个路径的数值
        stack_num = [root.val]
        while stack_node:
            c_node = stack_node[0]
            stack_node.remove(c_node)
            c_num = stack_num[0]
            stack_num.remove(c_num)
            # 叶子节点，把数值累加
            if not c_node.left and not c_node.right:
                total_num = total_num + c_num
                continue
            # 非叶子节点，把数值加到栈
            if c_node.left:
                stack_node.append(c_node.left)
                stack_num.append(c_num * 10 + c_node.left.val)
            if c_node.right:
                stack_node.append(c_node.right)
                stack_num.append(c_num * 10 + c_node.right.val)
        return total_num