# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot: return True

        def compare(root1, root2):
            que = [root1, root2]
            while que:
                node1=que.pop(0)
                node2=que.pop(0)
                if not node1 and not node2:continue
                if not node1 or not node2 or node1.val!=node2.val: return False
                que.append(node1.left)
                que.append(node2.left)
                que.append(node1.right)
                que.append(node2.right)
            return True

        stack = [root]
        while stack:
            node = stack.pop(-1)
            if node:
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop(-1)
                if compare(node, subRoot): return True
        return False

obj = Solution()
a1 = TreeNode(3)
a2 = TreeNode(4)
a3 = TreeNode(5)
a4 = TreeNode(1)
a5 = TreeNode(2)
a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5

b1 = TreeNode(4)
b2 = TreeNode(1)
b3 = TreeNode(2)
b1.left, b1.right = b2, b3
print(obj.isSubtree(a1, b1))