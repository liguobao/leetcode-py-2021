class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search_tow_sum(nums, target):
            sum = 0
            left = 0
            right = len(nums)-1
            while left < right:
                total = nums[left] + nums[right]
                # 当前和 小于 target, 左指针 + 1 
                # 左边的所有元素组合和都比Target小
                if total < target:
                    sum = sum + right - left
                    left = left +1
                else:
                    # 当前和大于taget，右指针 - 1
                    right = right -1
            return sum
        nums.sort()
        sum = 0
        for index, item in enumerate(nums):
            sub_target = target - item
            sub_sum = search_tow_sum(nums[index+1:], sub_target)
            sum = sum + sub_sum
        return sum
            
            

solution =Solution()
nums = [-2,0,1,3]
target = 2
results = solution.threeSumSmaller(nums, target)
print(f"nums:{nums},target:{target}")
print(f"{results}")