# 将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

# 作者：力扣(LeetCode)
# 链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from b_tree import BinaryTree, TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

    def sortedArrayToBST(self, nums):
        return self._sortedArrayToBST(nums, 0, len(nums) - 1)

    def _sortedArrayToBST(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        tree_node = TreeNode(nums[mid])
        tree_node.left = self._sortedArrayToBST(nums, start, mid - 1)
        tree_node.right = self._sortedArrayToBST(nums, mid + 1, end)
        return tree_node

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        level_array = []
        stack_node = [root]
        while stack_node:
            stack_len = len(stack_node)
            one_level_node = []
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                one_level_node.append(current_node.val)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len - 1
            level_array.append(one_level_node)
        return level_array


tree_array_1 = [-10, -3, 0, 5, 9]

# b_tree = BinaryTree(tree_array_1)
# solution_test = Solution()
# result = solution_test.isSymmetric(b_tree.root)
# print(result)


solution_test = Solution()
result = solution_test.sortedArrayToBST(tree_array_1)
print(result)
result = solution_test.levelOrder(result)
print(result)
