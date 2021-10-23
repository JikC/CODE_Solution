# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        dummy = Node(-1)
        dummy.next = head
        while head:  #
            node = Node(head.val)
            node.next = head.next
            head.next = node
            head = node.next
        head = dummy.next
        while head:
            head.next.random = head.random.next
            head = head.next.next
        head = dummy.next
        res = head.next
        while head:
            tmp = head.next
            if head.next:
                head.next = head.next.next
            head = tmp
        return res


obj = Solution()

print(obj.copyRandomList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]))
