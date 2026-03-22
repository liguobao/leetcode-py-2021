# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
# 返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

# 考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。

# nums 的前 k 个元素应包含 排序后 的唯一数字。下标 k - 1 之后的剩余元素可以忽略。

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2gy9m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4,_,_,_,_,_]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


class Solution(object):
    def removeDuplicates(self, nums):
        nums_size = len(nums)
        if nums_size ==0 :
            return 0 
        # 原地数组的索引
        sub_index = 0
        p_value = 0
        for i in range(0, nums_size):
            current_val = nums[i]
            if current_val == p_value:
                continue
            else:
                # 把当前数值，放到原地数组的按顺序位置
                sub_index = sub_index +1
                nums[sub_index] = current_val
            p_value = current_val
        return sub_index + 1
    

test_solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
result = test_solution.removeDuplicates(nums)
print(result)
