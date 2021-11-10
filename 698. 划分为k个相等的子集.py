class Solution:
    def canPartitionKSubsets(self, nums, k):
        if k==1: return True
        sums = sum(nums)
        if sums % k: return False
        n = len(nums)
        nums = sorted(nums, reverse=True)
        target = sums//k
        if nums[-1]>target: return False



obj=Solution()
print(obj.canPartitionKSubsets([4,3,2,3,5,2,1],4))

