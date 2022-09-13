class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [x for x in str(num)]
        max_n = max(nums)
        max_index = nums.index(max_n)
        print(f"max_index:{max_index},max_n:{max_n}")
        if max_index !=0:
            self.replace_nums(nums, max_n, max_index)
        else:
            sub_nums = nums[1:]
            sub_max_n = max(sub_nums)
            max_index = sub_nums.index(sub_max_n)
            self.replace_nums(sub_nums, sub_max_n, max_index)
            sub_nums.insert(0,max_n)
            nums = sub_nums
        return int("".join(nums))

    def replace_nums(self, nums, max_n, max_index):
        first_num = nums[0]
        nums[0] = max_n
        nums[max_index] = first_num


input_num = 98368
result = Solution().maximumSwap(input_num)
print(f"input_num:{input_num},result:{result}")
