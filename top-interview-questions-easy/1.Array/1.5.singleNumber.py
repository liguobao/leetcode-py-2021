# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        for item in nums:
            flag = flag ^ item
        return flag


nums = [1, 1, 3, 3, 6, 4, 4]
solution_test = Solution()
print(nums)
result = solution_test.singleNumber(nums)
print(result)
