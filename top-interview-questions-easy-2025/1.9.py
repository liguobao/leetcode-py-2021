# 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

# 你可以按任意顺序返回答案。

#  

# 示例 1：

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：

# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：

# 输入：nums = [3,3], target = 6
# 输出：[0,1]

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2jrse/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_size = len(nums)
        # 数字和它们的序号
        num_index_set = {}
        for i in range(nums_size):
            item = nums[i]
            if item not in num_index_set:
                num_index_set[item] = []
            # 把序号放在对应数组的最后
            num_index_set[item].append(i)
            secord_num = target - item
            # 找另一个数值所在的Index
            if secord_num in num_index_set and num_index_set[secord_num][0] != i:
                return [num_index_set[secord_num][0], i]
        return []
                
        