class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = {}
        for x in nums:
            if x not in nums_set:
                nums_set[x] = 0
            nums_set[x] = nums_set[x] + 1
        sum = 0
        for k in nums_set.keys():
            if nums_set[k] ==1:
                sum = sum + k
        return sum


result = Solution().sumOfUnique([1, 1, 1, 2, 2])
result = Solution().sumOfUnique([1, 1, 1, 1])
result = Solution().sumOfUnique([1, 1, 1, 1, 1])
