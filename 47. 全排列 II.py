def permuteUnique(nums):
    def dfs(nums, size, depth, path, used, res):
        if depth == size:
            res.append(path.copy())
            return
        for i in range(size):
            if not used[i]:
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: continue
                used[i]=True
                path.append(nums[i])
                dfs(nums, size, depth+1, path, used, res)
                used[i]=False
                path.pop()


    size = len(nums)
    if size == 0: return []
    nums.sort()
    used = [False] * len(nums)
    res = []
    dfs(nums, size, 0, [], used, res)
    return res

print(permuteUnique([1,1,1,2]))