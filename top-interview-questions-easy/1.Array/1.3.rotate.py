class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len == 0:
            return
        k = k % nums_len
        # 找到需要移动的位置，直接移动过去就完事了
        right_index = nums_len - k
        left_nums = nums[:right_index]
        right_nums = nums[right_index:]
        nums[:] = right_nums + left_nums


# 这个方法是一位位移动，性能不太好
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         nums_len = len(nums)
#         k = k % nums_len
#         if nums_len == 0:
#             return
#         for k_index in range(0, k):
#             change_value = nums[0]
#             for item_index in range(0, nums_len):
#                 next_index = item_index+1
#                 if next_index < nums_len:
#                     next_value = nums[next_index]
#                     nums[next_index] = change_value
#                     change_value = next_value
#                 else:
#                     nums[0] = change_value


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution_test = Solution()
print(nums, k)
solution_test.rotate(nums, k)
print(nums)
