# 计算给定二叉树的所有左叶子之和。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res


obj = Solution()
a1 = TreeNode(3)
a2 = TreeNode(9)
a3 = TreeNode(20)
a4 = TreeNode(15)
a5 = TreeNode(7)
a1.left, a1.right = a2, a3
a3.left, a3.right = a4, a5
print(obj.sumOfLeftLeaves(a1))
