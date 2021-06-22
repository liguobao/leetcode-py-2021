class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_set = {}
        for item_index in range(0, len(nums)):
            item_value = nums[item_index]
            if item_value in nums_set:
                nums_set[item_value].append(item_index)
            else:
                nums_set[item_value] = [item_index]
            secord_value = target - item_value
            if secord_value in nums_set and nums_set[secord_value][0] != item_index:
                return [item_index, nums_set[secord_value][0]]
        return []


nums = [3, 3]
target = 6
solution_test = Solution()
print(nums)
result = solution_test.twoSum(nums, target)
print(result)
