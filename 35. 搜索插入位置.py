# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        ans = len(nums)
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>=target:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans

obj = Solution()
print(obj.searchInsert([1,2,3,5,6],4))