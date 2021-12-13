
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

#  

# 示例 1:

# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # fn = max(f(n-1) * nums(n), nums(n))
        max_num = -1000000000
        imax =1
        imin =1
        for num_item in nums:
            # 由于存在负数，那么会导致最大的变最小的，最小的变最大的。
            # 因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
            # 出现负数的时候，把最大值和最小值交换
            if num_item <0:
                tmp = imax
                imax = imin
                imin = tmp
            imax = max(imax * num_item, num_item)
            imin = min(imin * num_item, num_item)
            max_num = max(max_num, imax)
        return max_num
            


solutuon = Solution()
nums = [-2,3,-4]
results = solutuon.maxProduct(nums=nums)
print(f"nums:{nums},result:{results}")
