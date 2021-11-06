class Solution:
    # 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
    def combine(selfself, n, k):
        res, path = [], []

        def backTrack(n, k, start):
            if len(path) == k: res.append(path.copy())
            for i in range(start, n + 1):
                path.append(i)
                backTrack(n, k, i + 1)
                path.pop(-1)

        backTrack(n, k, 1)
        return res


obj = Solution()
print(obj.combine(4, 2))
