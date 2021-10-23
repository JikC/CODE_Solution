class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # if len(nums1) > len(nums2):
        #     return self.findMedianSortedArrays(nums2, nums1)
        # m, n = len(nums1), len(nums2)
        # left, right = 0, m
        # midian1, median2 = 0, 0  # median1：前一部分的最大值; median2：后一部分的最小值
        # infinty = 10**6+1
        #
        # while left <= right:
        #     # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]; 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
        #     i = (left + right) // 2
        #     j = (m + n + 1) // 2 - i
        #
        #     m1 = -infinty if i == 0 else nums1[i-1]
        #     m2 =infinty if i==m else nums1[i]
        #     n1 =-infinty if j==0 else nums2[j-1]
        #     n2 =infinty if j==n else nums2[j]
        #
        #     if m1 <= n2:
        #         median1, median2 = max(m1, n1), min(m2, n2)
        #         left = i + 1
        #     else:
        #         right = i - 1
        #
        # return (median1 + median2) / 2.0 if (m + n) % 2 == 0 else median1
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement(totalLength// 2+1)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2



obj = Solution()
print(obj.findMedianSortedArrays([1, 3], [2, 4, 8, 9, 10]))
