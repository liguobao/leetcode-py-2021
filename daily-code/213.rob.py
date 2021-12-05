class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sub_rob(nums):
            f1 =0
            f2 =0
            sum =0
            # f(n) = max(f(n-2) + nums[n], f(n-1))
            for x in nums:
                sum = max(f2 + x , f1)
                f2 = f1
                f1 =sum
            return sum
        if len(nums) ==1:
            return nums[0]
        # 其实就是把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。
        first_nums = nums[0:len(nums)-1]
        second_nums = nums[1:len(nums)]
        return max(sub_rob(first_nums), sub_rob(second_nums))

solutuon = Solution()
nums = [2, 3, 2]
result = solutuon.rob(nums=nums)
print(f"nums:{nums},result:{result}")

nums = [2]
result = solutuon.rob(nums=nums)
print(f"nums:{nums},result:{result}")
