# 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。

#  

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false
#  

# 提示:

# 1 <= s.length, t.length <= 5 * 104
# s 和 t 仅包含小写字母
#  

# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？




# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn96us/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        # 两者字符串理应是有相同的字符数量
        # 一个加进去，一个减掉
        all_char={}
        for c in s:
            if c not in all_char:
                all_char[c]=0
            all_char[c] = all_char[c] +1
        for c in t:
            if c not in all_char:
                all_char[c]=0
            all_char[c] = all_char[c] -1
        for value in all_char.values():
            if value !=0:
                return False
        return True
    
s_value = "aacc"
t_value = "ccac"
print(s_value)
solution_test = Solution()
result = solution_test.isAnagram(s_value, t_value)
print(result)