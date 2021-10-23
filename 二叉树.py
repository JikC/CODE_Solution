class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isAVL(self, root):
        if not root: return True
        self.res = True

        def depth(root):
            if not root: return 0
            L = depth(root.left)
            R = depth(root.right)
            if abs(L - R) > 1:
                self.res = False
            return max(R, L) + 1

        depth(root)
        return self.res

    def preorderTraversal(self, root):
        # 前序遍历-迭代-LC144_二叉树的前序遍历
        res = []
        if not root: return res
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
                res.append(node.val)
        return res

    def postorderTraversal(self, root):
        # 后序遍历-迭代-LC145_二叉树的后序遍历
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop(-1)
            res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res[::-1]

    def inorderTraversal(self, root):
        # 中序遍历-迭代-LC94_二叉树的中序遍历
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop(-1)
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop(-1)
                res.append(node.val)
        return res

    def levelOrder(self, root):
        res = []
        if not root: return res
        que = [root]
        while que:
            node = que.pop(0)
            res.append(node.val)
            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
        return res

    def levelOrderBottom(self, root):
        # 107. 二叉树的层序遍历 II
        results = []
        if not root: return results
        que = [root]
        while que:
            result = []
            for _ in range(len(que)):
                node = que.pop(0)
                result.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            results.append(result)
        return results[::-1]

    # def invertTree(self, ):



obj = Solution()
a1 = TreeNode(10)
a2 = TreeNode(6)
a3 = TreeNode(3)
a4 = TreeNode(9)
a5 = TreeNode(16)
a1.left, a1.right = a2, a5
a2.left, a2.right = a3, a4
print(obj.isAVL(a1))
print(obj.preorderTraversal(a1))
print(obj.postorderTraversal(a1))
print(obj.inorderTraversal(a1))
print(obj.levelOrder(a1))
print(obj.levelOrderBottom(a1))
