# 字符串中的第一个唯一字符
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

#  

# 示例 1：

# 输入: s = "leetcode"
# 输出: 0
# 示例 2:

# 输入: s = "loveleetcode"
# 输出: 2
# 示例 3:

# 输入: s = "aabb"
# 输出: -1
#  

# 提示:

# 1 <= s.length <= 105
# s 只包含小写字母



# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn5z8r/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_size = len(s)
        char_dict={}
        char_list = []
        for index in range(s_size):
            item = s[index]
            if item not in char_dict:
                char_dict[item]=0
                char_list.append({"char":item, "index":index})
            char_dict[item] = char_dict[item] + 1
        for char_item in char_list:
            char_key = char_item["char"]
            if char_dict[char_key] ==1:
                return char_item["index"]
        return -1

s_value = "leetcode"
print(s_value)
solution_test = Solution()
result = solution_test.firstUniqChar(s_value)
print(result)