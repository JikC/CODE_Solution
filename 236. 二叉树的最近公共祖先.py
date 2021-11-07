# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==p or root==q or not root: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root
        elif left: return left
        elif right: return right
        else: return None

a1 = TreeNode(3)
a2 = TreeNode(5)
a3 = TreeNode(1)
a4 = TreeNode(6)
a5 = TreeNode(2)
a6 = TreeNode(0)
a7 = TreeNode(8)
a8 = TreeNode(7)
a9 = TreeNode(4)
a1.left, a1.right = a2,a3
a2.left, a2.right = a4,a5
a3.left, a3.right = a6,a7
a5.left, a5.right = a8,a9
obj = Solution()
print(obj.lowestCommonAncestor(a1,a4,a9).val)
