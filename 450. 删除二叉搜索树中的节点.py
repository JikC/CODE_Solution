# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PrintTree:

    def levelOrder(self, root):
        res = []
        if not root: return res
        que = [root]
        while que:
            size = len(que)
            for i in range(size):
                cur = que.pop(0)
                # if cur:
                res.append(cur.val if cur else None)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return res


class Solution:
    def deleteNode(self, root, key):
        if not root:  # 第一种情况：没找到删除的节点，遍历到空节点直接返回
            return root

        if root.val == key:
            if not root.left and not root.right:  # 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
                del root
                return None
            elif not root.right:  # 第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
                tmp = root
                root = root.left
                del tmp
                return root
            elif not root.left:  # 第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
                tmp = root
                root = root.right
                del tmp
                return root
            else:  # 第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                tmp = root
                root = root.right
                del tmp
                return root
        if root.val > key:  # 左递归
            root.left = self.deleteNode(root.left, key)
        if root.val < key:  # 右递归
            root.right = self.deleteNode(root.right, key)
        return root


obj = Solution()
a1 = TreeNode(5)
a2 = TreeNode(3)
a3 = TreeNode(6)
a4 = TreeNode(2)
a5 = TreeNode(4)
a6 = TreeNode(7)
a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5
a3.right = a6

ob = PrintTree()
print(ob.levelOrder(a1))  # [5, 3, 6, 2, 4, 7]
obj = Solution()
result = obj.deleteNode(a1, 3)
print(ob.levelOrder(result))
