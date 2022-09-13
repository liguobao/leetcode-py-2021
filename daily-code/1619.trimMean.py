class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        arr_len = len(arr)
        cut_size = int(arr_len * 0.05)
        cut_array = arr[cut_size:arr_len-cut_size]
        return sum(cut_array) / len(cut_array)


arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
result = Solution().trimMean(arr)
print(result)
