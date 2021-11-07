# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。output:list[],eg.[2,3]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root):
        if not root: return
        res = []
        stack = []
        pre, cur = None, root
        maxcount, count = 0, 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                if not pre:
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1
                if count == maxcount:
                    res.append(cur.val)
                elif count > maxcount:
                    maxcount = count
                    res = []
                    res.append(cur.val)
                pre = cur
                cur = cur.right
        return res


a1, a2, a3, a4, a5 = TreeNode(3), TreeNode(2), TreeNode(2), TreeNode(3), TreeNode(1)
a1.left, a2.left, a2.right, a3.left = a2, a3, a4, a5
obj = Solution()
print(obj.findMode(a1))
