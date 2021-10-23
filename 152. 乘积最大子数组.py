class Solution:
    def maxProduct(self, nums):
        maxF, minF, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx, mn = maxF, minF
            maxF = max(mx * nums[i], max(nums[i], mn * nums[i]))
            minF = min(mn * nums[i], min(nums[i], mx * nums[i]))
            ans = max(ans, maxF)
        return ans


obj = Solution()
print(obj.maxProduct([2,3,-2,4]))
