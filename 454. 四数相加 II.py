# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
#     0 <= i, j, k, l < n
#     nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
import collections


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hashmap = collections.defaultdict(int)
        for x1 in nums1:
            for x2 in nums2:
                hashmap[x1 + x2] += 1
        count = 0
        for x3 in nums3:
            for x4 in nums4:
                count += hashmap[0 - x3 - x4]
        return count


obj = Solution()
print(obj.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
