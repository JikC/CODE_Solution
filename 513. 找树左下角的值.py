# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
# 假设二叉树中至少有一个节点。
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.maxdepth = -1

        def traversal(root, depth):
            if not root.left and not root.right:
                if depth > self.maxdepth:
                    self.maxdepth = depth
                    self.leftval = root.val
            if root.left:
                traversal(root.left, depth + 1)
            if root.right:
                traversal(root.right, depth + 1)

        traversal(root, 0)
        return self.leftval

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)
a1.left, a1.right = a2, a3
a2.left, a3.left, a3.right = a4, a5, a6
a5.left = a7
obj = Solution()
print(obj.findBottomLeftValue(a1))

