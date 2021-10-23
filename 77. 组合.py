class Solution:
    def combine(selfself, n, k):
        res, path = [], []
        def backTrack(n, k, start):
            if len(path)==k:
                res.append(path.copy())
                return
            for i in range(start, n+1):
                path.append(i)
                backTrack(n, k, i+1)
                path.pop(-1)
        backTrack(n, k, 1)
        return res

obj = Solution()
print(obj.combine(4,2))