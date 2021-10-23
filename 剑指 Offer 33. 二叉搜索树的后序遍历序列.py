class Solution:
    def verifyPostorder(self, postorder):
        def recur(i, j):
            if i >= j: return True  # 此子树节点数量≤1 ，无需判别正确性
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p  # 寻找第一个大于根节点的节点，索引记为m
            while postorder[p] > postorder[j]: p += 1
            # 判断此树是否正确；判断此树的左子树是否正确； 判断此树的右子树是否正确
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


obj = Solution()
print(obj.verifyPostorder([1, 3, 2, 6, 5]))
