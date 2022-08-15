
# https://leetcode.cn/problems/maximum-binary-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.build_tree(nums)
        return root
    
    
    def build_tree(self, nums):
        if len(nums)==0:
            return None
        max_num, max_num_index = self.find_max_num(nums)
        left_nums = nums[:max_num_index]
        right_nums = nums[max_num_index+1:]
        root = TreeNode(max_num)
        root.left = self.build_tree(left_nums)
        root.right = self.build_tree(right_nums)
        return root
        
        
        

    # 寻找数组中最大的元素，返回该元素和下标
    def find_max_num(self, nums):
        index = 0
        max_num = max(nums)
        for x in nums:
            if x == max_num:
                break
            index = index + 1
        return max_num, index


nums = [3, 2, 1, 6, 0, 5]
result = Solution().constructMaximumBinaryTree(nums)
print(result)
