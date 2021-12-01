class Soulution():

    def search(self, nums, left, right):
        mid = (right + left) // 2
        # 终止条件，是三个值
        if len(nums[left:right + 1]) == 3:
            return nums[right] if nums[left] == nums[left + 1] else nums[left]
        mid_value = nums[mid]
        # input_values = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        # input_values = [1, 2, 2, 3, 3, 4, 4, 5, 5]
        # input_values = [1, 1, 2, 2, 3, 3, 5]
        # 中值 == 右边
        if mid_value == nums[mid + 1]:
            # 中值下标 是偶数位 + 中值右侧 == 中值，说明 单个数值在右边
            # 如[1, 1, 2, 2, 3, 3, 4, 4, 5]
            if mid % 2 == 0:
                return self.search(nums, mid, right)
            else:
                # [1, 2, 2, 3, 3,4, 4]
                return self.search(nums, left, mid - 1)
        elif mid_value == nums[mid - 1]:
            # 中值等于左边，中值下标是偶数，说明单数值在右边
            # 如 [1, 2, 2, 3, 3, 4, 4, 5, 5]
            if mid % 2 == 0:
                return self.search(nums, left, mid)
            else:
                # [1, 1, 2, 2, 3, 3,4]
                return self.search(nums, mid + 1, right)
        else:
            return mid_value


soulution = Soulution()
input_values = [1, 1, 2, 2, 3, 3,4]
left = 0
right = len(input_values) - 1
result = soulution.search(input_values, left, right)
print(f"input_values:{input_values}\nresult:{result}")

input_values = [1, 2, 2, 3, 3,4, 4]
left = 0
right = len(input_values) - 1
result = soulution.search(input_values, left, right)
print(f"input_values:{input_values}\nresult:{result}")


input_values = [1, 2, 2]
left = 0
right = len(input_values) - 1
result = soulution.search(input_values, left, right)
print(f"input_values:{input_values}\nresult:{result}")


input_values = [1, 1, 2, 2, 3, 3, 4, 4, 5]
left = 0
right = len(input_values) - 1
result = soulution.search(input_values, left, right)
print(f"input_values:{input_values}\nresult:{result}")


input_values = [1, 2, 2, 3, 3, 4, 4, 5, 5]
left = 0
right = len(input_values) - 1
result = soulution.search(input_values, left, right)
print(f"input_values:{input_values}\nresult:{result}")


input_values = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
left = 0
right = len(input_values) - 1
result = soulution.search(input_values, left, right)
print(f"input_values:{input_values}\nresult:{result}")
