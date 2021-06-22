class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        new_nums = []
        zero_nums = 0
        for item_index in range(0, nums_len):
            item_value = nums[item_index]
            if item_value != 0:
                new_nums.append(item_value)
            else:
                zero_nums = zero_nums+1
        for z_index in range(0, zero_nums):
            new_nums.append(0)
        nums[:] = new_nums


nums = [0, 1, 0, 3, 12]
solution_test = Solution()
print(nums)
solution_test.moveZeroes(nums)
print(nums)
