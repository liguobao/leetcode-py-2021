class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right )//2
            x = nums[mid]
            if x == target:
                return mid
            elif x < target:
                left = mid +1
            else:
                right = mid -1
        return -1

solution = Solution()
input_list = [-1, 1]
target = 10
result = solution.search(input_list, target)
print(f"input_list:{input_list},target:{target},result:{result}")
