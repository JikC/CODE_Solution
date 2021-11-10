class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return
        head = Node(-1)
        prev = head
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop(-1)
            prev.right = cur
            cur.left = prev
            prev = cur
            cur = cur.right
        head.right.left = prev
        prev.right = head.right

        return head.right

a1 = Node(4)
a2 = Node(2)
a3 = Node(5)
a4 = Node(1)
a5 = Node(3)
a1.left, a1.right, a2.left, a2.right = a2, a3, a4, a5
obj = Solution()
res = obj.treeToDoublyList(a1)
print(res.left.val, res.right.val)