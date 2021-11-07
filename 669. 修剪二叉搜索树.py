# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。
#
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # # 1. digui
        # if not root: return root
        # if root.val < low:
        #     return self.trimBST(root.right, low, high)
        # if root.val > high:
        #     return self.trimBST(root.left, low, high)
        # root.left = self.trimBST(root.left, low, high)
        # root.right = self.trimBST(root.right, low, high)
        # return root
        if not root: return root
        while root and (root.val<low or root.val>high):
            if root.val<low: root = root.right
            else: root = root.left
        cur = root
        while cur:
            while cur.left and cur.left.val<low:
                cur.left = cur.left.right
            cur = cur.left
        cur = root
        while cur:
            while cur.right and cur.right.val>high:
                cur.right = cur.right.left
            cur = cur.right
        return root
