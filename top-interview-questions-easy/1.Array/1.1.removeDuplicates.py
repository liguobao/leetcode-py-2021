class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_index = 0
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        p_value = nums[0]
        for item_index in range(0, nums_len):
            item_value = nums[item_index]
            # 当前值和上一个值相同
            if p_value == item_value:
                continue
            else:
                # 上一个值和当前值不一样，则考虑把当期值设置到占位Index
                s_index = s_index + 1
                nums[s_index] = item_value
            p_value = item_value
        return s_index + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 9, 10]
solution_test = Solution()
print(nums)
new_len = solution_test.removeDuplicates(nums)
print(new_len)
print(nums)
