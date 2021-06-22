class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        for array_item in intervals:
            if not merged_intervals:
                merged_intervals.append(array_item)
                continue
            latest_merged_item = merged_intervals[-1]
            if latest_merged_item[1] < array_item[0]:
                merged_intervals.append(array_item)
            else:
                latest_merged_item[1] = max(latest_merged_item[1],array_item[1])
        return merged_intervals



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
solution = Solution()
result = solution.merge(intervals)
print(f"nums:{intervals},result:{result}")

intervals = [[1, 4], [4, 5]]
solution = Solution()
result = solution.merge(intervals)
print(f"nums:{intervals},result:{result}")
