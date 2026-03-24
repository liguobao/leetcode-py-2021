# 合并两个有序数组
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

#  

# 示例 1：

# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

# 作者：LeetCode
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnumcr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        merged = []        # 存放最终结果
        p1 = 0             # nums1 指针
        p2 = 0             # nums2 指针
        # 1. 同时遍历两个数组，谁小放谁
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        # 2. 把剩余元素补上（只会发生在其中一个数组）
        merged.extend(nums1[p1:m])
        merged.extend(nums2[p2:n])
        
        # 3. 覆盖写回 nums1（原地修改）
        nums1[:] = merged