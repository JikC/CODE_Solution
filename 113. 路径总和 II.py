# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):
        if not root: return []
        res = []
        path = [root.val]

        def traversal(root, count):
            if not root.left and not root.right and count == 0:
                res.append(path[:])
                return
            if not root.left and not root.right: return
            if root.left:
                path.append(root.left.val)
                traversal(root.left, count - root.left.val)
                path.pop(-1)
            if root.right:
                path.append(root.right.val)
                traversal(root.right, count - root.right.val)
                path.pop(-1)

        traversal(root, targetSum - root.val)
        return res


a1 = TreeNode(5)
a2 = TreeNode(4)
a3 = TreeNode(8)
a4 = TreeNode(11)
a5 = TreeNode(13)
a6 = TreeNode(4)
a7 = TreeNode(7)
a8 = TreeNode(2)
a9 = TreeNode(1)
a10 = TreeNode(5)
a1.left, a1.right = a2, a3
a2.left, a3.left, a3.right = a4, a5, a6
a4.left, a4.right = a7, a8
a6.left, a6.right = a10, a9
obj = Solution()
print(obj.pathSum(a1, 22))