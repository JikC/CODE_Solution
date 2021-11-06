class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def preorderTraversal(self, root):
        res = []

        def traversal(root):
            if not root: return root
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return res