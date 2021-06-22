class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = {}
        for item in nums:
            if item in nums_set:
                return True
            else:
                nums_set[item] = item
        return False


nums = [7, 1, 5, 3, 6, 4, 4]
solution_test = Solution()
print(nums)
result = solution_test.containsDuplicate(nums)
print(result)
