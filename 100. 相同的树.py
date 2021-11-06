class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
        # 输入：p = [1,2,3], q = [1,2,3]；输出：true
        que = [p, q]
        while que:
            node1 = que.pop(0)
            node2 = que.pop(0)
            if not node1 and not node2: continue
            if not node1 or not node2 or node1.val != node2.val: return False
            que.append(node1.left)
            que.append(node2.left)
            que.append(node1.right)
            que.append(node2.right)
        return True
