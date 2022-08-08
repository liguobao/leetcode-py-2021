from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        def compare_val(x,y):
            return 1 if int(x+y) < int(y+x) else -1
        nums_text = [str(x) for x in nums]
        nums_text.sort(key=cmp_to_key(compare_val))
        result = "".join(nums_text)
        if result[0]=="0":
            return "0"
        return result


nums = [1, 7, 90, 5]
print(Solution().largestNumber(nums))
