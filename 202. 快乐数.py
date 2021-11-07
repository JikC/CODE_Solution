# 编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」定义为：
#     对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
#     然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
#     如果 可以变为  1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。
# 示例 1：
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n = n // 10
            return s

        record = set()
        while True:
            n = getSum(n)
            if n == 1: return True
            if n in record:
                return False
            else:
                record.add(n)


obj = Solution()
print(obj.isHappy(19))
