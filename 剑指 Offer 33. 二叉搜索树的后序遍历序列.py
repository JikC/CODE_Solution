class Solution:
    def verifyPostorder(self, postorder):
        # 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop(-1)
            stack.append(postorder[i])
        return True


obj = Solution()
print(obj.verifyPostorder([1, 6, 3, 2, 5]))  # False
print(obj.verifyPostorder([1, 3, 2, 6, 5]))  # True
