# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

# 现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

# 给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-length-of-pair-chain
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        pairs.sort()
        dp = [1] * n
        # dp[i] = max(dp[i], dp[j] +1 )
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
pairs = [[1,2], [3,4],[2,3]]
result = Solution().findLongestChain(pairs)
print(f"pairs:{pairs},result:{result}")