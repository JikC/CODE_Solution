class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 给定一个二叉树，检查它是否是镜像对称的。例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        if not root: return True
        que = [root.left, root.right]
        while que:
            L = que.pop(0)
            R = que.pop(0)
            if not L and not R:
                continue
            if not L or not R or L.val!=R.val:
                return False
            que.append(L.left)
            que.append(R.right)
            que.append(L.right)
            que.append(R.left)
        return True