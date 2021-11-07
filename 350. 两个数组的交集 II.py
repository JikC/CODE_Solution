# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
import collections


class Solution:
    def intersect(self, nums1, nums2):
        res = []
        n = collections.defaultdict(int)
        for i in nums1:
            n[i] += 1
        for i in nums2:
            if n[i] > 0: res.append(i)
            n[i] -= 1
        return res


obj = Solution()
print(obj.intersect([1, 2, 2, 3], [2, 2]))
