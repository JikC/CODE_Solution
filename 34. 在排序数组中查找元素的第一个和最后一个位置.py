# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
class Solution:
    def searchRange(self, nums, target):
        def search(nums, target, lower):
            left, right, ans = 0, len(nums) - 1, len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (lower and nums[mid] >= target):
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            return ans

        leftidx = search(nums, target, True)
        rightidx = search(nums, target, False) - 1
        if leftidx <= rightidx and rightidx < len(nums) and nums[leftidx] == target and nums[rightidx] == target:
            return [leftidx, rightidx]
        return [-1, -1]


obj = Solution()
print(obj.searchRange([5, 7, 7, 7, 8, 8, 10], 7))
