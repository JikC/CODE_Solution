class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val: return root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)


a1 = TreeNode(4)
a2 = TreeNode(2)
a3 = TreeNode(7)
a4 = TreeNode(1)
a5 = TreeNode(3)
a1.left, a1.right = a2,a3
a2.left, a2.right = a4,a5
obj = Solution()
res = obj.searchBST(a1,2)
print(res.val, res.left.val, res.right.val)
