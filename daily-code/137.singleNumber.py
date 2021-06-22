class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single_nums = set()
        nums_map ={}
        for num_item in nums:
            if num_item not in nums_map:
                nums_map[num_item] = 0
                single_nums.add(num_item)
            nums_map[num_item] = nums_map[num_item]+1
            if nums_map[num_item] >1 and num_item in single_nums:
                single_nums.remove(num_item)
        return list(single_nums)[0]
        
        
nums = [2,2,3,2]
solution = Solution()
result = solution.singleNumber(nums)
print(f"nums:{nums},result:{result}")

nums = [0,1,0,1,0,1,99]
solution = Solution()
result = solution.singleNumber(nums)
print(f"nums:{nums},result:{result}")