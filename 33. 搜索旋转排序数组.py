class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if nums[left] == target: return left
        if nums[right] == target: return right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[mid] < nums[right]:  # 右半段有序
                if nums[mid] < target <= nums[right]:  # 如果target在右半段，则移动左边界
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # 左半段有序
                if nums[left] <= target < nums[mid]:  # 如果target在左半段，则移动右边界
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
# 时间复杂度: O(logn)