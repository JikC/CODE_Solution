# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
class Solution:
    def spiralOrder(self, matrix):
        res = []
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n - 1, 0, m - 1
        while True:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            if up + 1 > down: break
            up += 1
            
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            if right - 1 < left: break
            right -= 1

            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            if down - 1 < up: break
            down -= 1

            for i in range(down, up + 1, -1):
                res.append(matrix[i][left])
            if left + 1 > right: break
            left += 1
        return res


obj = Solution()
print(obj.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
