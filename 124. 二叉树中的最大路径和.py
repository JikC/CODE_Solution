# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
# class MyTree(object):
#     def __init__(self, root):
#         self.root = TreeNode()
#         self.dep = 0
#     def construct(self, nums):
#         for i in range(len(nums)):
#             if self.root

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if root == None: return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.res = max(self.res, root.val + left + right)
            return max(left, right) + root.val

        self.res = root.val
        dfs(root)
        return self.res


if __name__ == '__main__':
    a1 = TreeNode(-10)
    a2 = TreeNode(9)
    a3 = TreeNode(20)
    a4 = TreeNode(15)
    a5 = TreeNode(7)
    a1.left, a1.right = a2, a3
    a3.left, a3.right = a4, a5
    s = Solution()
    print(s.maxPathSum(a1))
