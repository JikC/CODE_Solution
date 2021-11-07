# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。
#     4
#    / \
#   2   6
#  / \
# 1   3   output:1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = float("inf")
        stack = []
        pre = None
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                if pre:
                    res = min(res, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return res


a1, a2, a3, a4, a5 = TreeNode(4), TreeNode(2), TreeNode(6), TreeNode(1), TreeNode(3)
a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5
obj = Solution()
print(obj.getMinimumDifference(a1))
