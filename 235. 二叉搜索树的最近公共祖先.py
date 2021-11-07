class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if p.val<root.val and q.val<root.val:
            left = self.lowestCommonAncestor(root.left, p,q)
            if left: return left
        if p.val>root.val and q.val>root.val:
            right = self.lowestCommonAncestor(root.right,p,q)
            if right: return right
        return root








a1 = TreeNode(6)
a2 = TreeNode(2)
a3 = TreeNode(8)
a4 = TreeNode(0)
a5 = TreeNode(4)
a6 = TreeNode(7)
a7 = TreeNode(9)
a8 = TreeNode(1)
a9 = TreeNode(3)
a10 = TreeNode(5)
a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5
a3.left, a3.right = a6, a7
a5.left, a5.right = a9, a10
a4.right = a8
obj = Solution()
print(obj.lowestCommonAncestor(a1, a4, a10).val)
