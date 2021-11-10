class Solution:
    def findLength(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        res = 0
        for i in range(1,m+1):
            for j in range(n, 0, -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                res = max(dp[j], res)
        return res


obj = Solution()
print((obj.findLength([1, 2, 3, 2, 1], [4, 3, 2, 1, 7, 6])))
