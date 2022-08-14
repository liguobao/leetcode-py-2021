class Solution(object):

    def cal_score(self, s, num):
        return len([x for x in s if x == num])

    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max(self.cal_score(s[:i], "0") + self.cal_score(s[i:], "1") for i in range(1,len(s)))


s = "011101"
result = Solution().maxScore(s)
print(f"{s},result:{result}")
