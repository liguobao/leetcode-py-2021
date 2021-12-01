class Soulution():

    def search(self, nums):
        left = 0
        right = len(nums)
        mid = (right - left) // 2
        while left <= right:
            mid_value = nums[mid]
            pass
        return -1


soulution = Soulution()
input_values = [1, 1, 2, 3, 3]
result = soulution.search(input_values)
print(f"input_values:{input_values},result:{result}")

input_values = [1, 1, 2]
result = soulution.search(input_values)
print(f"input_values:{input_values},result:{result}")


input_values = [1, 2, 2]
result = soulution.search(input_values)
print(f"input_values:{input_values},result:{result}")


input_values = [1, 1, 2, 2, 3, 3, 4, 4, 5]
result = soulution.search(input_values)
print(f"input_values:{input_values},result:{result}")


input_values = [1, 2, 2, 3, 3, 4, 4, 5, 5]
result = soulution.search(input_values)
print(f"input_values:{input_values},result:{result}")


input_values = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
result = soulution.search(input_values)
print(f"input_values:{input_values},result:{result}")
