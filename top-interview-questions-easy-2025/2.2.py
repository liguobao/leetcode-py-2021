# 整数反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

# 假设环境不允许存储 64 位整数（有符号或无符号）。
#  

# 示例 1：

# 输入：x = 123
# 输出：321
# 示例 2：

# 输入：x = -123
# 输出：-321
# 示例 3：

# 输入：x = 120
# 输出：21
# 示例 4：

# 输入：x = 0
# 输出：0

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnx13t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ==0:
            return 0
        first_num = x >0
        new_x = x if first_num else -x
        result = 0
        while new_x !=0:
            result = result * 10
            # 取余
            end_num = new_x % 10 
            result  = result + end_num
            new_x = int(new_x /10)
        if not first_num:
            result = - result
        if result < - 2**31 or result > 2**31:
            return 0
        return result    
        
        