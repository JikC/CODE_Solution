# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
class Solution:
    def minSubArrayLen(self, target, nums):
        res = float("inf")
        sums = 0
        index = 0
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= target:
                res = min(res, i - index + 1)
                sums -= nums[index]
                index += 1
        return 0 if res == float("inf") else res


obj = Solution()
print(obj.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
