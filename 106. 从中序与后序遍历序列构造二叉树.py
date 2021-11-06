class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#    3
#   / \
#  9  20
#    /  \
#   15   7

class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder: return None
        rootval = postorder[-1]
        root = TreeNode(rootval)
        separator_idx = inorder.index(rootval)
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder) - 1]
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root


obj = Solution()
root = obj.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

