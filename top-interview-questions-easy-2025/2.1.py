# 反转字符串
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

#  

# 示例 1：

# 输入：s = ["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 示例 2：

# 输入：s = ["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
#  

# 提示：

# 1 <= s.length <= 105
# s[i] 都是 ASCII 码表中的可打印字符

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnhbqj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s_size = len(s)
        m_index = int(s_size /2 )
        for item_index in range(0, m_index):
            current_item = s[item_index]
            # 5 - 0 - 1 
            repace_index = s_size - item_index -1
            s[item_index] = s[repace_index]
            s[repace_index] = current_item
        return s
    
s_text = ["h", "e", "l", "l", "o"]
print(s_text)
solution_test = Solution()
result = solution_test.reverseString(s_text)
print(result)