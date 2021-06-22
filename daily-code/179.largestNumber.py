
from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 自定义比较函数，"34" + "3" < "3"+"34", 则 334，否则倒过来
        def cmp(x, y):
            return 1 if x + y < y+x else -1
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))
        first_num = nums[0]
        if first_num == "0":
            return 0
        return str("".join(nums))


nums = [1, 4, 6, 60]
solution = Solution()
result = solution.largestNumber(nums)
print(f"nums:{nums},largestNumber:{result}")


nums = [0, 0]
solution = Solution()
result = solution.largestNumber(nums)
print(f"nums:{nums},largestNumber:{result}")
