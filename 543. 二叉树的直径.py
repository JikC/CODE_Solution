# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def depth(root):
            if not root: return 0
            L = depth(root.left)
            R = depth(root.right)
            self.res = max(self.res, L+R)
            return max(L, R)+1
        depth(root)
        return self.res

obj = Solution()
a1 = TreeNode(5)
a2 = TreeNode(3)
a3 = TreeNode(6)
a4 = TreeNode(2)
a5 = TreeNode(4)
a6 = TreeNode(7)
a7 = TreeNode(7)
a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5
a3.right = a6
a6.right = a7


obj = Solution()
result = obj.diameterOfBinaryTree(a1)
print(result)