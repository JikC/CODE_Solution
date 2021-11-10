class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        r1, r2 = -1, -1
        for i in range(len(nums)):
            if nums[i] < 2:
                r2 += 1
                nums[i], nums[r2] = nums[r2], nums[i]
                if nums[r2] < 1:
                    r1 += 1
                    nums[r1], nums[r2] = nums[r2], nums[r1]
        return nums


obj = Solution()
print(obj.sortColors([2, 0, 1, 1, 0, 2, 0, 0]))
