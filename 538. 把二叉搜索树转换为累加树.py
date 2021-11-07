# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root):
        # # 1.
        # self.pre = 0
        #
        # def traversal(root):
        #     if not root: return
        #     traversal(root.right)
        #     root.val += self.pre
        #     self.pre = root.val
        #     traversal(root.left)
        #
        # traversal(root)
        # return root
        pre = 0
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop(-1)
                cur.val += pre
                pre = cur.val
                cur = cur.left
        return root

