# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
# 叶子节点 是指没有子节点的节点。
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root: return False
        que = [[root, root.val]]
        while que:
            node = que.pop(0)
            if not node[0].left and not node[0].right and node[1] == targetSum: return True
            if node[0].left:
                que.append([node[0].left, node[1] + node[0].left.val])
            if node[0].right:
                que.append([node[0].right, node[1] + node[0].right.val])
        return False


a1 = TreeNode(5)
a2 = TreeNode(4)
a3 = TreeNode(8)
a4 = TreeNode(11)
a5 = TreeNode(13)
a6 = TreeNode(4)
a7 = TreeNode(7)
a8 = TreeNode(2)
a9 = TreeNode(1)
a1.left, a1.right = a2, a3
a2.left, a3.left, a3.right = a4, a5, a6
a4.left, a4.right = a7, a8
a6.right = a9
obj = Solution()
print(obj.hasPathSum(a1, 22))
