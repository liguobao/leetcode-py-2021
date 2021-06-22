from b_tree import BinaryTree


# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
# 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
class Solution(object):
    def _sub_path_sum(self, tree_node, path_array, tar):
        # 当前节点是None，直接返回
        if tree_node is None:
            return
        # 现在的target数值 减去当前的节点数值 = 0 且 节点是叶子节点没有子节点，则此路径符合要求
        if tar - tree_node.val == 0 and not tree_node.left and not tree_node.right:
            path_array.append(tree_node.val)
            self.result_array.append(list(path_array))
        # 递归循环左右节点，每次剩余target = 当前Target 减去当前值
        # 同时将当前值填入子序列中
        self._sub_path_sum(tree_node.left, path_array +
                           [tree_node.val], tar - tree_node.val)
        self._sub_path_sum(tree_node.right, path_array +
                           [tree_node.val], tar - tree_node.val)

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        self.target = target
        self.result_array = []
        if root is None:
            return self.result_array
        self._sub_path_sum(root, [], target)
        return self.result_array


tree_array = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
target = 22
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
result = Solution().pathSum(b_tree.root, target)
print(f"result:{result}")
