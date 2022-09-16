import heapq as h


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        head = nums[:k]
        # k个堆，由小到大的堆，最后在head中第一个元素就是第K大的
        h.heapify(head)
        n = len(nums)
        # 剩下的元素，依次遍历
        for x in range(k, n):
            x_val = nums[x]
            # 当前值大于最小值
            # -> head中的最小值被移除，往head加入当前值
            if x_val > head[0]:
                h.heappop(head)
                h.heappush(head, x_val)
        return head[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
result = Solution().findKthLargest(nums, k)
print(result)
