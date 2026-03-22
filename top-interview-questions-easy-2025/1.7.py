# 加一
# 给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。

# 将大整数加 1，并返回结果的数字数组。

#  

# 示例 1：

# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 加 1 后得到 123 + 1 = 124。
# 因此，结果应该是 [1,2,4]。
# 示例 2：

# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 加 1 后得到 4321 + 1 = 4322。
# 因此，结果应该是 [4,3,2,2]。
# 示例 3：

# 输入：digits = [9]
# 输出：[1,0]
# 解释：输入数组表示数字 9。
# 加 1 得到了 9 + 1 = 10。
# 因此，结果应该是 [1,0]。
#  

# 提示：

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits 不包含任何前导 0。

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2cv1c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_size = len(digits)
        # 前一次进位得到的数值
        x_value = 1
        # 从最后往前面走
        for num_index in range(digits_size -1, -1, -1):
            num = digits[num_index]
            # 当前 加上 进位过来的数
            current_num = num + x_value
            # 计算完的数值，%10之后往当前位置放
            digits[num_index] = current_num % 10
            # 进位要不是0，要不是1
            x_value = 1 if current_num >9 else 0
        # 最后如果进位还是有的，应该要补0
        if x_value >0:
            digits.insert(0, x_value)
        return digits

nums = [9]
solution_test = Solution()
print(nums)
solution_test.plusOne(nums)
print(nums)
