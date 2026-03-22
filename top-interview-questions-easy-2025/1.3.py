# 旋转数组
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

#  

# 示例 1:

# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:

# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
#  

# 提示：

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len ==0:
            return 
        # K 可能 比 Num的长度大
        k = k % nums_len
        # 最要需要移动的位置坐标
        right_index = nums_len - k
        left_nums = nums[:right_index]
        right_nums = nums[right_index:]
        nums[:] = right_nums + left_nums
        return
        