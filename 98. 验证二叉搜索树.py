# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        pre = -float("inf")
        cur = root
        stack = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                if cur.val < pre.val: return False
                pre = cur
                cur = cur.right
        return True
