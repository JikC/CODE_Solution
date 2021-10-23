class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        res = []
        size = len(candidates)

        def dfs(path, sums, depth):
            if sums > target or depth==size:
                return
            if sums == target:
                res.append(path)
                return
            for i in range(depth, size):
                if sums + candidates[i]>target:
                    break
                dfs(path+[candidates[i]], sums+candidates[i], i)

        dfs([], 0, 0)
        return res


obj = Solution()
print(obj.combinationSum([5, 3, 2], 8))
