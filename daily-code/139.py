# 139. 单词拆分
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

# 示例 1：

# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

# https://leetcode-cn.com/problems/word-break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        s_count = len(s)
        # dp[i] 表示 前s[0:i]是否能被空格拆分成若干个wordDict出现的单词
        dp = [False] * (s_count + 1)
        dp[0] = True
        for i in range(1, s_count+1):
            # 从 j 到 i 
            for j in range(0, i):
                # 判断 j -> i 之间的词是否在词典里面
                # 且 dp[j] 可以被拆分
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[s_count]


s = "leetcode"
wordDict = ["leet", "code"]
result = Solution().wordBreak(s, wordDict)
print(f"s:{s},wordDict:{wordDict},result:{result}")

s = "a"
wordDict = ["a"]
result = Solution().wordBreak(s, wordDict)
print(f"s:{s},wordDict:{wordDict},result:{result}")
