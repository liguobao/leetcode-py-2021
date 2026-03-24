# 二叉树的层序遍历
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

#  

# 示例 1：


# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：

# 输入：root = [1]
# 输出：[[1]]
# 示例 3：

# 输入：root = []
# 输出：[]
#  

# 提示：

# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnldjj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        results=[]
        if root is None:
            return []
        stack_node =deque([root])
        while stack_node:
            curent_count = len(stack_node)
            curent_values = []
            while curent_count >0:
                current_node = stack_node.popleft()
                curent_values.append(current_node.val)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                curent_count = curent_count -1
            results.append(curent_values)
        return results
        
        