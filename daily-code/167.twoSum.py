# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
# 给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

#  
# 示例 1：

# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

# 示例 2：

# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]


# 示例 2：

# 输入：numbers = [2,3,4], target = 5
# 输出：[1,2]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left +1, right +1]
            # 当前和 小于 target, 左指针 + 1 
            if total < target:
                left = left +1
            else:
                # 当前和大于taget，右指针 - 1
                right = right -1


solution = Solution()
numbers = [2, 7, 11, 15]
target = 9
result = solution.twoSum(numbers, target)
print(f"numbers:{numbers},target:{target},result:{result}")
