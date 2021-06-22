
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。

# 说明: 叶子节点是指没有子节点的节点。
from b_tree import BinaryTree


class Solution(object):
    def _dsf(self, tree_node, paths, res):
        # 当前节点是空，直接返回
        if tree_node is None:
            return
        paths = paths + str(tree_node.val)
        # 当前节点是最底部的叶子节点，这个路走完了，把整个路径填入数组
        if not tree_node.left and not tree_node.right:
            res.append(paths)
            return res
        # 对左边和右边都执行一次
        self._dsf(tree_node.left,  paths + "->", res)
        self._dsf(tree_node.right, paths + "->", res)
        return res

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root is None:
            return res
        self._dsf(root, "", res)
        return res


tree_array = [1, 2, 3, None, 5]
b_tree = BinaryTree(tree_array)
result = Solution().binaryTreePaths(b_tree.root)
print(f"result:{result}")
