class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums_len = len(digits)
        x_value = 1
        for item_index in range(nums_len-1, -1, -1):
            item_value = digits[item_index]
            c_value = (item_value + x_value)
            x_value = 1 if c_value > 9 else 0
            digits[item_index] = c_value % 10
        if x_value > 0:
            digits.insert(0, x_value)
        return digits


nums = [9]
solution_test = Solution()
print(nums)
solution_test.plusOne(nums)
print(nums)
