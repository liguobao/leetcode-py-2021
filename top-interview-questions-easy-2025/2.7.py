# 实现 strStr()
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

#  

# 示例 1：

# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 示例 2：

# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#  

# 提示：

# 1 <= haystack.length, needle.length <= 104
# haystack 和 needle 仅由小写英文字符组成



# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnr003/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_size = len(needle)
        if needle_size ==0:
            return -1
        first_value = needle[0]
        haystack_size = len(haystack)
        for i in range(haystack_size):
            h_value = haystack[i]
            if h_value == first_value and haystack[i:i+needle_size] == needle:
                return i
        return -1

haystack = "hello"
needle = "ll"
print(f"haystack:{haystack},needle:{needle}")
solution_test = Solution()
result = solution_test.strStr(haystack, needle)
print(result)
