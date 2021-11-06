# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点。
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        if not root: return []
        res = []

        def backtrack(root, path):
            if not root: return
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path.copy())
            ways = []
            if root.left: ways.append(root.left)
            if root.right: ways.append(root.right)
            for way in ways:
                backtrack(way, path)
                path.pop(-1)

        backtrack(root, [])
        return res


obj = Solution()
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(5)

a1.left, a1.right = a2, a3
a2.right = a4
print(obj.binaryTreePaths(a1))
