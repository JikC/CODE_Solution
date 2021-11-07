# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            if num / mid == mid:
                return True
            elif num / mid > mid:
                left += 1
            elif num / mid < mid:
                right -= 1
        return False


obj = Solution()
print(obj.isPerfectSquare(10))
