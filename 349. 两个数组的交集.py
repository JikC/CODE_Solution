class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


obj = Solution()
print(obj.intersection([1, 2], [2, 3, 3, 4]))
