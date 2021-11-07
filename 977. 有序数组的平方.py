# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]

class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        left, right, k = 0, n - 1, n - 1
        ans = [0] * n
        while left <= right:
            lm = nums[left] ** 2
            rm = nums[right] ** 2
            if lm > rm:
                ans[k] = lm
                left += 1
            else:
                ans[k] = rm
                right -= 1
            k -= 1
        return ans


obj = Solution()
print(obj.sortedSquares([-4, -1, 0, 3, 10]))
