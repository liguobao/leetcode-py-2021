class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        new_nums = []
        min_nums = nums2 if nums2_len < nums1_len else nums1
        max_nums = nums1 if nums2_len < nums1_len else nums2
        for item in min_nums:
            if item in max_nums:
                new_nums.append(item)
                max_nums.remove(item)
        return new_nums


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
solution_test = Solution()
print(nums1, nums2)
result = solution_test.intersect(nums1, nums2)
print(result)
