# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from b_tree import BinaryTree


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 构建父节点字典
        parent_dict = self.to_dict_by_dfs(root)
        # print(parent_dict)
        # 从p构建节点父节点Set
        visited_val = set()
        # 不断寻找p节点的父级节点
        while p !=None:
            visited_val.add(p.val)
            # 节点不存在父级节点，终止循环
            p = parent_dict.get(p.val, None)
        # 遍历 q节点，如果q节点已经是p节点父级节点里面了
        # 说明此时的q就是我们要的公共节点
        while q != None:
            if q.val in visited_val:
                return q
            q = parent_dict.get(q.val, None)
        return None

    def to_dict_by_dfs(self, root):
        parent_dict = {}
        # 深度优先
        def dfs(root):
            # 左节点存在，左节点的值的父节点为Root
            if root.left:
                parent_dict[root.left.val] = root
                dfs(root.left)
            # 右节点同理
            if root.right:
                parent_dict[root.right.val] = root
                dfs(root.right)
            return
        dfs(root)
        return parent_dict
            
            


root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
tree_root = BinaryTree(root)
result = Solution().lowestCommonAncestor(tree_root.root, p, q)
